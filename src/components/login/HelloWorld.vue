<template>
  <div class="login FlexCSHC">
    <!-- <div class="imgabc">
      <img src="../assets/img/xjst.png" />
    </div> -->
    <div class="loginCardBox FlexRCE">
      <div class="loginCard">
        <h1 class="h1 FlexRCC">FireWatchPro</h1>

        <el-form
          ref="ruleFormRef"
          class="pageBox"
          label-width="0"
          :model="ruleForm"
          :rules="rules"
        >
          <el-form-item prop="username">
            <usernameInput
              class="inputWar"
              :type="form1type1"
              v-model:value="ruleForm.username"
              placeholder="请输入用户名"
            >
            </usernameInput>
          </el-form-item>
          <el-form-item prop="password">
            <passwordInput
              class="inputWar"
              :type="form1type2"
              v-model:value="ruleForm.password"
              placeholder="请输入用户密码"
            >
            </passwordInput>
          </el-form-item>
        </el-form>
        <el-button
          :loading="loading"
          :disabled="loading"
          type="primary"
          class="button"
          size="large"
          @click="loginUp()"
          >登录</el-button
        >
      </div>
    </div>
    <!-- <div class="bottombk">
      {{
        "Copyright©北京先进数通信息技术股份公司 All Rights Reserved 京ICP备09069393号-1"
      }}
    </div> -->
    
  </div>
  
</template>
<script setup>
import { ref, reactive, watch, onMounted, onUnmounted } from "vue";
import usernameInput from "./intpuBox/usernameInput.vue";
import passwordInput from "./intpuBox/passwordInput.vue";
import { useRouter } from 'vue-router'
const router = useRouter()
const ruleFormRef = ref();
const oncevalidate = ref(true);
const loading = ref(false);
const ruleForm = reactive({
  username: "",
  password: "",
});
watch(ruleForm, () => {
  if (oncevalidate.value == false) {
    ruleFormRef.value.validate((valid) => {});
  }
});
const form1type1 = ref("normal");
const form1type2 = ref("normal");
const validatePass = (rule, value, callback) => {
  if (value === "") {
    callback("请输入密码");
    form1type2.value = "error";
  } else {
    form1type2.value = "normal";
    callback();
  }
};
const validateUsername = (rule, value, callback) => {
  if (value === "") {
    callback("请输入用户名");
    form1type1.value = "error";
  } else {
    form1type1.value = "success";
    callback();
  }
};
const rules = {
  username: [{ validator: validateUsername, trigger: "blur" }],
  password: [{ validator: validatePass, trigger: "blur" }],
};
const loginUp = () => {
  ruleFormRef.value.validate((valid) => {
    oncevalidate.value = false;
    if (valid) {
      router.push({ name: 'TopNavbar' })
    }
  });
};
</script>

<style lang="less" scoped>
.imgabc {
  position: absolute;
  left: 0;
  bottom: 0;
  margin-bottom: 350px;
  margin-left: 210px;

  img {
    display: inline-block;
    width: 300px;
  }
}
.login {
  position: relative;
  width: 100vw;
  height: 100vh;
  background-image: url("../document/img/login_banner.jpg");
  background-repeat: no-repeat;
  background-size: cover;

  .loginCardBox {
    width: 100%;
    // max-width: 1024px;
    max-width: 1200px;
    height: 100%;
    margin: 0 auto;
  }
  .loginCard {
    box-sizing: border-box;
    width: 464px;
    height: 459px;
    padding: 42px 49px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 0 20px 0 rgb(0 0 0 / 0.2);

    .h1 {
      // font-family: PangMenZhengDao, sans-serif;
      font-weight: bold; /* 标准加粗 */
      font-weight: 1000;
      font-size: 43px;
      font-style: normal;
      line-height: 1;
      color: #4072ed;
      text-align: left;
    }
    .pageBox {
      margin-top: 68px;
    }
    .button {
      width: 100%;
      margin-top: 10px;
      background: var(--el-color-primary);
      // background: red;
    }
  }
}
:deep(.el-button--large) {
  border-radius: 16px;
}
.bottombk {
  width: 100%;
  text-align: center;
  position: absolute;
  bottom: 0;
  font-size: 12px;
  margin-bottom: 10px;
  color: #fff;
}
:deep(.el-form-item__content) {
  line-height: 100% !important;
}
</style>
