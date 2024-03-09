<template>
  <div class="cube smaller" @click="rotateCube" :style="cude_st">
    <div class="face front">
      <div class="inner">{{ faces[0] }}</div>
    </div>
    <div class="face back">
      <div class="inner">{{ faces[1] }}</div>
    </div>
    <div class="face right">
      <div class="inner">{{ faces[2] }}</div>
    </div>
    <div class="face left">
      <div class="innerr">{{ faces[3] }}</div>
    </div>
    <div class="face top">
      <div class="innerr">{{ faces[4] }}</div>
    </div>
    <div class="face bottom">
      <div class="innerr">{{ faces[5] }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faces: [
        "བོད་སྨན།", "ཤན་འབྱེད་", "སྔོ་སྨན་","藏药", "识别",  "藏花"
      ],
      cude_st:{
        position:"absolute", /* 设置绝对定位 */
        top: "80px", /* 距离顶部的距离 */
        left:"140px",/* 距离左侧的距离 */
        width:"100px",
        height:"100px"
      },
      currentFaceIndex: 0
    };
  },
  methods: {
    rotateCube() {
      this.currentFaceIndex = (this.currentFaceIndex + 1) % 6; // 循环切换到下一个面
    }
  }
};
</script>

<style scoped>
.cube {
  width: 100px; /* 将宽度设为原来的一半 */
  height: 100px; /* 将高度设为原来的一半 */
  position: relative;
  transform-style: preserve-3d;
  animation: rotateCube 10s infinite; /* 调整旋转动画的持续时间 */
}

.face {
  position: absolute;
  width: 100px;
  height: 100px;
  line-height: 100px;
  text-align: center;
  font-size: 30px;
  color: white;
  background-color: black;
  word-wrap: break-word;
  overflow: hidden;
  max-width: 100%;
  max-height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid white; /* 添加白色边框 */
}

.inner {
  transform: translateY(-10px); /* 向上移动10px */
}

.front  { transform: translateZ(50px); }
.back   { transform: rotateY(180deg) translateZ(50px); }
.right  { transform: rotateY(90deg) translateZ(50px); }
.left   { transform: rotateY(-90deg) translateZ(50px); }
.top    { transform: rotateX(90deg) translateZ(50px); }
.bottom { transform: rotateX(-90deg) translateZ(50px); }

@keyframes rotateCube {
  from { transform: rotateX(0deg) rotateY(0deg); }
  to { transform: rotateX(360deg) rotateY(360deg); }
}
</style>
