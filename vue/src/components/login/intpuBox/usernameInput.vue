<script  setup>
import { CircleCloseFilled, SuccessFilled, User } from '@element-plus/icons-vue';
import { computed, defineModel } from 'vue';

defineOptions({ name: 'usernameInput' });
const value = defineModel("value", { });
const props = defineProps({
  placeholder: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'normal'
  }
});
const ErrorColor = computed(() => {
  if (props.type === 'error') {
    return '#EC0000';
  }
  return undefined
})
</script>
<template>
  <div class="inputBox FlexRCS input-war"
    :class="{ normal: props.type === 'normal' || props.type === 'success', error: props.type === 'error' }">
    <div class="imgWar FlexCCC">
      <slot name="leftName">
        <el-icon :size="20" :color="ErrorColor ? ErrorColor : '#656565'">
          <User />
        </el-icon>
      </slot>
    </div>
    <hr class="hr" />
    <div class="center">
      <div class="inH FlexCSHB">
        <div class="name">账号</div>
        <input type="text" class="input" maxlength="50" v-model="value" @blur="$emit('blur', value)" :placeholder="placeholder" />
      </div>
    </div>
    <div class="right FlexRCC">
      <el-icon v-if="props.type === 'error'" size="16" color="#EC0000">
        <CircleCloseFilled />
      </el-icon>
      <el-icon v-if="props.type === 'success'" size="16" color="rgba(67, 65, 95, 1)">
        <SuccessFilled />
      </el-icon>
    </div>
  </div>
</template>
<style lang="less" scoped>
input:focus-visible {
  outline: 0;
  outline-offset: 0;
}

.inputBox.error {
  border-color: #EC0000;
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
}

</style>


