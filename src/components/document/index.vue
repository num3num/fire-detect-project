<template>
  <div class="box">
    <!-- <div class="top">
      <h1>FireWatchPro</h1>
    </div> -->
    <div class="content">
      <div class="contentForm">
        <el-form
          ref="formRef"
          :inline="false"
          :model="mdl"
          :rules="rules"
          class="demo-form-inline"
        >
          <el-form-item
            label="图片/视频预览 :"
            label-width="110px"
            style="margin-bottom: 10px"
          >
            <!-- -->
            <el-upload
              accept="image/png,image/jpeg,image/gif,video/mp4"
              action="#"
              list-type="picture-card"
              :limit="1"
              :auto-upload="false"
              :file-list="fileList"
              :on-change="handleUploadChange"
              :disabled="uploadDisabled"
            >
              <el-icon><Plus /></el-icon>

              <template #file="{ file }">
                <div v-if="file.raw.type !== 'video/mp4'">
                  <img
                    class="el-upload-list__item-thumbnail"
                    :src="file.url"
                    alt=""
                  />
                  <span class="el-upload-list__item-actions">
                    <span
                      class="el-upload-list__item-preview"
                      @click="handlePictureCardPreview(file, true)"
                    >
                      <el-icon><zoom-in /></el-icon>
                    </span>
                    <span
                      v-if="!disabled"
                      class="el-upload-list__item-delete"
                      @click="handleRemove(file)"
                    >
                      <el-icon><Delete /></el-icon>
                    </span>
                  </span>
                </div>
                <div v-else>
                  <video :src="file.url"></video>
                  <span class="el-upload-list__item-actions">
                    <span
                      class="el-upload-list__item-preview"
                      @click="handlePictureCardPreview(file, false)"
                    >
                      <el-icon><zoom-in /></el-icon>
                    </span>
                    <span
                      v-if="!disabled"
                      class="el-upload-list__item-delete"
                      @click="handleRemove(file)"
                    >
                      <el-icon><Delete /></el-icon>
                    </span>
                  </span>
                </div>
              </template>
            </el-upload>
            <el-dialog v-model="dialogVisible">
              <img
                v-if="isImg"
                :src="dialogImageUrl"
                alt="Preview Image"
                width="100%"
              />
              <video controls v-else :src="dialogImageUrl" width="100%"></video>
            </el-dialog>
          </el-form-item>
          <el-form-item
            label="图片路径:"
            prop="file_path"
            label-width="110px"
            style="margin-bottom: 20px"
            ><el-input
              v-model="mdl.file_path"
              style="width: 300px; margin-right: 5px"
              placeholder="请输入图片或视频路径"
            />
          </el-form-item>
          <el-form-item
            label="输出路径:"
            prop="sava_path"
            label-width="110px"
            style="margin-bottom: 20px"
            ><el-input
              v-model="mdl.sava_path"
              style="width: 300px; margin-right: 5px"
              placeholder="请输入输出路径"
            />
          </el-form-item>
          <el-form-item label-width="110px"
            ><el-button
              type="primary"
              @click="handleChange"
              style="width: 150px"
              >发送</el-button
            >
            <!-- 安全策略导致无法读取前端给的路径 -->
            <!-- <el-button type="primary" :disabled="btnDisabled" @click="imgClick" style="width: 150px"
              >图片预览</el-button
            > -->
          </el-form-item>
        </el-form>
        <div class="remind">
          <!-- <div>
            <el-dialog v-model="imgDialogVisible">
              {{ isDialogImageUrl }}
              <img
                v-if="isImgClick"
                :src="isDialogImageUrl"
                alt="Preview Image"
                width="100%"
              />
              <video
                controls
                v-else
                :src="isDialogImageUrl"
                width="100%"
              ></video>
            </el-dialog>
          </div> -->
          <div v-if="showContent == 0">
            <div>提示:无事发生</div>
            <div v-html="content"></div>
          </div>
          <div v-if="showContent == 1">
            <div style="color: red">提示:有浓烟,可能发生火灾</div>
            <div>{{ content }}</div>
          </div>
          <div v-if="showContent == 2">
            <div style="color: red">提示:着火了,有浓烟</div>
            <div v-html="content"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, reactive, watch, onMounted, onUnmounted } from "vue";
import { Upload, Plus, ZoomIn, Delete } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import { docUpload } from "./api/index";
const showContent = ref(0);
const content = ref("森林防火,人人有责");
const mdl = ref({
  file_path: "",
  sava_path: "",
});
const formRef = ref();
const rules = {
  file_path: [
    { required: true, message: "路径不能为空", trigger: "blur" },
    {
      pattern: /^[A-Za-z0-9]:\//,
      message: "路径必须以字母盘符开头（如C:/）",
      trigger: ["blur", "change"],
    },
  ],
  sava_path: [
    { required: true, message: "路径不能为空", trigger: "blur" },
    {
      pattern: /^[A-Za-z]:\\/,
      message: "路径必须以字母盘符开头（如C:\）",
      trigger: ["blur", "change"],
    },
  ],
};
const fileNamePath = ref("");
const ext = ref("");
const fileNameSava = ref("");
const dialogImageUrl = ref("");
const isDialogImageUrl = ref("");
const dialogVisible = ref(false);
const imgDialogVisible = ref(false);
const disabled = ref(false);
const uploadDisabled = ref(false);
const fileList = ref([]);
const isImgClick = ref(false);
const btnDisabled = ref(true);
// const imgClick = () => {
//   imgDialogVisible.value = true;

//   if (ext.value !== "mp4") {
//     isImgClick.value = true;
//   } else {
//     isImgClick.value = false;
//   }
//   // let imageUrl = "";
//   // fileNamePath.value = mdl.value.file_path.substring(
//   //   mdl.value.file_path.lastIndexOf("/") + 1
//   // );
//   // ext.value = fileNamePath.value.split(".").pop();
//   // fileNameSava.value = mdl.value.sava_path + "\\";
//   // imageUrl = `file://${fileNameSava.value}${fileNamePath.value}`;
//   // isDialogImageUrl.value =imgSrc
//   // isDialogImageUrl.value = fileNameSava.value + "\\" + fileNamePath.value;
// };
const handleUploadChange = (file, files) => {
  uploadDisabled.value = true;
  fileList.value = [files[files.length - 1]]; // 覆盖逻辑
};
const handleRemove = (file) => {
  fileList.value = [];
  uploadDisabled.value = false;
};
const isImg = ref(false);
const handlePictureCardPreview = (file, flag) => {
  dialogImageUrl.value = file.url;
  dialogVisible.value = true;
  isImg.value = flag;
};
const handleDownload = (file) => {
  console.log(file);
};

const handleChange = () => {
  formRef.value.validate((valid) => {
    if (valid) {
      fileNamePath.value = mdl.value.file_path.substring(
        mdl.value.file_path.lastIndexOf("/") + 1
      );
      ext.value = fileNamePath.value.split(".").pop();
      fileNameSava.value = mdl.value.sava_path;
      // 校验通过后的提交逻辑
      docUpload(mdl.value)
        .then((data) => {
          ElMessage({
            message: data,
            type: null,
            center: true, // 使消息居中显示
            duration: 2000,
          });
          btnDisabled.value = false;
          if (
            data.message == "Warning,fire is detected,and there is smoke" ||
            data.message == "Warning,fire is detected"
          ) {
            console.log("data.message", data.message);
            showContent.value = 2;
            content.value = `
        1. **逆风方向逃生‌**:火势顺风蔓延速度可达8公里/小时，逆风逃生可争取更多时间。&zwnj;<br>
        2. **湿物防护‌**:用湿毛巾或衣物捂住口鼻，降低吸入有毒烟尘的风险。<br>
        3. **选择安全区域‌**：优先避开植被密集区，选择裸岩、河滩等不易燃烧区域,若被困，可利用已燃烧区域（地表温度较低）作为临时避难所。
        <br>4. **现场处置**：如果火势较小，现场人员可使用灭火器等设备进行初期灭火；若火势较大，应立即撤离并等待专业消防队伍处理。
       <br> 5.**衣物着火处理**‌：立即停步、倒地翻滚灭火，缩短燃烧时间。**点火解围‌：在无法逃离时，点燃周围植被形成隔离带，但需与火线保持安全距离。
        <br>6.**预防措施**:选择安全营地‌：远离枯草、灌木区域，清理火源周边3米内可燃物。看管火源‌：确保火源全程有人值守，熄灭后需用水浸透灰烬直至无余温。 ‌
       <br> 7.**若火势无法控制，建议立即拨打火警电话119并准确报告位置。
        `;
          } else if (
            data.message == "Warning,smoke is detected,may cause fire"
          ) {
            showContent.value = 1;
            content.value = `
        1. **判断火势与风向**:立即观察火势大小和风向，选择逆风方向逃生，避免顺风跑动。若被大火包围，应快速向山下或空旷地带撤离，切勿向山林深处或低洼地逃生。<br>
        2. **防护与撤离‌**:用湿毛巾或衣物捂住口鼻，低姿势（手膝着地）沿消防通道或楼梯撤离。切忌乘坐电梯，普通电梯井易形成“烟囱效应”加剧危险。<br>
        3. **无法撤离时自救‌**：若无法逃离，立即封闭门缝防止浓烟侵入，用明显颜色衣物在窗口发出求救信号（如红色外套），并保持冷静等待救援。
        <br>4. **衣物着火处理**：若衣物着火应迅速脱下或打滚灭火，避免皮肤烧伤。切勿奔跑，以免加速空气流通导致火势加剧。
        `;
          } else {
            showContent.value = 0;
            content.value = `森林防火,人人有责`;
          }
        })
        .catch((error) => {
          console.error("======================:", error);
          // 处理上传失败的逻辑，例如重试机制等
        });
    } else {
      console.log(22);
      return false;
    }
  });
};
</script>

<style lang="less" scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.box {
  overflow: hidden;
  background: #eff6ff;
  width: 100vw;
  height: 91vh;
}
.top {
  width: 100%;
  height: 10%;

  // text-align: center;
  padding-left: 20px;
  display: flex;
  align-items: center;
  box-shadow: 0 0 20px 0 rgb(0 0 0 / 0.2);
  border-bottom: 1px solid #f5f6f9;
}
.content {
  width: 100%;
  height: 100%;
  // padding: 20px 10px 10px 10px;
}
.contentForm {
  width: 50%;
  height: 100%;
  margin: 0 auto;
  padding-left: 5px;
  padding-top: 5px;
  background: #fff;
  // border: 3px solid #f5f6f9;
}
.remind {
  border-top: 3px solid #f5f6f9;
  margin-top: 5px;
}
</style>
