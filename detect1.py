import argparse
import os
import platform
import shutil
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, plot_one_box, strip_optimizer)
from utils.torch_utils import select_device, load_classifier, time_synchronized

def detect(source,output):
    output = output if output else 'yolov5/inference/output'
    weights='./best.pt'
    img_size=640
    conf_thres=0.4
    iou_thres=0.5
    device='cpu'
    view_img=False
    save_txt=False
    agnostic_nms=False
    augment=False
    update=False
    save_img=False
    classes=0

    # 判断是否是视频/摄像头流
    webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')

    # 初始化
    device = select_device(device)
    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)
    half = device.type != 'cpu'

    # 加载模型
    model = attempt_load(weights, map_location=device)
    img_size = check_img_size(img_size, s=model.stride.max())
    if half:
        model.half()

    # 是否加载二阶段分类器
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])
        modelc.to(device).eval()

    # 加载数据
    vid_path, vid_writer = None, None
    if webcam:
        view_img = True
        cudnn.benchmark = True
        dataset = LoadStreams(source, img_size=img_size)
    else:
        save_img = True
        dataset = LoadImages(source, img_size=img_size)

    # 类别名称和颜色
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

    # 推理初始化
    t0 = time.time()
    img = torch.zeros((1, 3, img_size, img_size), device=device)
    _ = model(img.half() if half else img) if device.type != 'cpu' else None

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()
        img /= 255.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        t1 = time_synchronized()
        pred = model(img, augment=augment)[0]
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes, agnostic=agnostic_nms)
        t2 = time_synchronized()

        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        for i, det in enumerate(pred):
            if webcam:
                p, s, im0 = path[i], f'{i}: ', im0s[i].copy()
            else:
                p, s, im0 = path, '', im0s

            save_path = str(Path(output) / Path(p).name)
            txt_path = str(Path(output) / Path(p).stem) + (f'_{dataset.frame}' if dataset.mode == 'video' else '')
            s += f'{img.shape[2]}x{img.shape[3]} '
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]

            if det is not None and len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()
                    s += f'{n} {names[int(c)]}s, '

                for *xyxy, conf, cls in det:
                    if save_txt:
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * 5 + '\n') % (cls, *xywh))

                    if save_img or view_img:
                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

            print(f'{s}Done. ({t2 - t1:.3f}s)')

            if view_img:
                cv2.imshow(p, im0)
                if cv2.waitKey(1) == ord('q'):
                    raise StopIteration

            if save_img:
                if dataset.mode == 'images':
                    cv2.imwrite(save_path, im0)
                else:
                    if vid_path != save_path:
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()
                        fourcc = 'mp4v'
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        print(f'Results saved to {Path(output)}')
        if platform.system() == 'Darwin' and not update:
            os.system('open ' + save_path)

    print(f'Done. ({time.time() - t0:.3f}s)')
    return save_path



if __name__ == '__main__':
    
    with torch.no_grad(): 
        detect(source='inference/images/fire.mp4',output='inference/output')
