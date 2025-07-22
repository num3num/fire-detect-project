<!-- TopNavbar.vue -->
<template>
  <div class="homeBox">
    <div class="contentForm">
      <div style="margin-left: 5px;">
        野火危害
      </div>
      <el-carousel :interval="2000" type="card" height="200px">
        <el-carousel-item>
          <img src="./img/ts.webp" alt="" width="100%" />
        </el-carousel-item>
        <el-carousel-item>
          <img src="./img/ts1.webp" alt="" width="100%" />
        </el-carousel-item>
        <el-carousel-item>
          <img src="./img/slfh5.jpg" alt="" width="100%" />
        </el-carousel-item>

        <el-carousel-item>
          <img src="./img/slfh6.jfif" alt="" width="100%" />
        </el-carousel-item>
      </el-carousel>
      <div class="contentVideo">
        <video src="./img/tssp.mp4" width="100%" controls></video>
      </div>
    
    </div>
  </div>
</template>

<style lang="less" scoped>
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.homeBox {
  overflow: hidden;
  background: #eff6ff;
  width: 100vw;
  height: 91vh;
}
.contentForm {
  //     width: 50%;
  //   height: 100%;
  //   margin: 0 auto;
  //   padding-left: 5px;
  //   padding-top: 5px;
  //    background: #fff;
  width: 50%;
  height: 100%;
  margin: 0 auto;
  position: relative;
  background: #fff;
  padding-top: 5px;
}
.quadrant {
  position: absolute;
  width: 50%;
  height: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
}
.top-left {
  top: 0;
  left: 0;
  border-right: 1px solid #eee;
  border-bottom: 1px solid #eee;
}
.top-right {
  top: 0;
  right: 0;
  border-bottom: 1px solid #eee;
}
.bottom-left {
  bottom: 0;
  left: 0;
  border-right: 1px solid #eee;
}
.bottom-right {
  bottom: 0;
  right: 0;
}
.contentVideo{
  margin-top: 10px;
  width: 100%;
  height: 60%;
  // background: red;
}
</style>
