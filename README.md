# fire-detect-project
about fire,smoke and warning，是一个前后端分离项目
### 安装环境
```
    python: 3.6+
    ubuntu16.04 or 18.04
    darknet (cuda10.0 docker) ***
    pytorch 1.6+ (cuda10.2 docker)
```

启动方式：
```shell
conda create -n fire_env python=3.10 -y
conda activate fire_env

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

测试方式：
```
# 方式1：
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/detect?file_path={file_path}&sava_path={sava_path}' \
  -H 'accept: application/json' \
  -d ''

# 方式2：
localhost:port/docs#
```


前端启动方式见 /vue目录下README
