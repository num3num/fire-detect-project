<script setup>
import { Hide, Key, View } from '@element-plus/icons-vue';
import { computed, nextTick, ref } from 'vue';

defineOptions({ name: 'passwordInput' });
const value = defineModel("value", {  });
const props = defineProps({
  placeholder: {
    type: String,
    default: ''
  },
  // placeholder: String,
  type: {
    type: String,
    default: 'normal'
  },
  name: {
    type: String,
    default: ''
  }
});
let passwordType = ref(true);
const passwordTypeShow = computed(() => {
  if (passwordType.value) {
    return 'password';
  } else {
    return 'text';
  }
});
const ErrorColor = computed(() => {
  if (props.type === 'error') {
    return '#EC0000';
  }
  return undefined;
});
function handlePasswordType() {
  let valueP = value.value
  passwordType.value = !passwordType.value
  nextTick(() => {
    value.value = valueP;
  })
}
</script>
<template>
  <div class="inputBox FlexRCS input-war" :class="{ normal: props.type === 'normal', error: props.type === 'error' }">
    <div class="imgWar FlexCCC">
      <slot name="leftName">
        <el-icon class="deg45" :size="20" :color="ErrorColor ? ErrorColor : '#656565'">
          <Key />
        </el-icon>
      </slot>
    </div>
    <hr class="hr" />
    <div class="center">
      <div class="inH FlexCSHB">
        <div class="name">{{ props.name != '' ? props.name : '密码' }}</div>
        <input :type="passwordTypeShow" maxlength="50" class="input" @blur="$emit('blur', value)" v-model="value"
          :placeholder="placeholder" />
      </div>
    </div>
    <div class="right FlexRCC">
      <el-icon :size="20" color="#656565" @click.stop="handlePasswordType">
        <View v-if="!passwordType" />
        <Hide v-if="passwordType" />
      </el-icon>
    </div>
  </div>
</template>


<style scoped lang="less">
input:focus-visible {
  outline: 0;
  outline-offset: 0;
}

.inputBox.error {
  border-color: #EC0000;
}

.right .el-icon {
  cursor: pointer;
}

.input-war() {
  box-sizing: border-box;
  width: 100%;
  height: 55px;
  padding: 9px 0;
  background: #FFF;
  border: 2px solid #F0F0F2;
  border-radius: 12px;

  .hr {
    width: 0;
    height: 100%;
    margin: 0;
    border: 0;
    border-left: 1px solid #E7E7E7;
  }

  .deg45 {
    transform: rotate(45deg);
  }

  .imgWar {
    flex: 1 0 54px;
    width: 54px;
    height: 100%;

    .leftImage {
      width: 20px;
      height: auto;
    }
  }

  .center {
    width: 100%;
    height: 100%;

    .inH {
      box-sizing: border-box;
      height: 100%;
      padding: 0 8px;
    }

    .name {
      font-family: PingFangMedium, sans-serif;
      font-size: 9px;
      font-weight: 400;
      color: #909090;
    }

    .input {
      padding: 0;
      font-size: 16px;
      font-weight: bold;
      color: #303030;
      border: 0;
    }
    
    .input::placeholder {
      font-family: PingFangMedium, sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: #E0E0E0;
    }
  }

  .right {
    flex: 1 0 54px;
    width: 54px;
  }
}

.inputBox {
  .input-war();
  
  .leftName .icon {
    transform: rotate(45deg);
  }
}
</style>


