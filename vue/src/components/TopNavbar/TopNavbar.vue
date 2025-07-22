<!-- TopNavbar.vue -->
<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
  >
    <!-- 添加文字Logo -->
    <el-menu-item index="logo" disabled class="logo-item">
      <span style="font-weight: bold; font-size: 24px">FireWatchPro</span>
    </el-menu-item>
    <el-menu-item index="1">首页</el-menu-item>
    <el-menu-item index="2">火情实况</el-menu-item>
  </el-menu>
  <div class="content">
    <Document v-if="activeIndex === '2'" />
    <home v-if="activeIndex === '1'" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Document from "../document/index.vue";
import home from "../home/index.vue";
const activeIndex = ref("1"); // 默认激活的菜单项索引值
const handleSelect = (key, keyPath) => {
  if (key !== "logo") {
    // 防止点击logo时触发
    activeIndex.value = key;
    console.log(key, keyPath);
  }
};
</script>
<style>
.logo-item {
  cursor: default !important;
  opacity: 1 !important;
  
}
.logo-item:hover {
  background-color: transparent !important;
}
</style>
