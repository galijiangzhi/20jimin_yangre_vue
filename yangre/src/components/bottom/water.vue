<template>
    <div :style="ro_st">
      <div class="father-div">
        <div class="container">
          <div class="dot1"></div>
          <div class="dot2"></div>
          <div class="dot2"></div>
          <div class="dot3"></div>
          <div class="dot4"></div>
          <div class="dot5"></div>
          <div class="dot6"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        ro_st: {
          width: "126px",
        //   backgroundColor: "red",
          position: "absolute",
          top:"850px",
          left:"1400px"
        },
      };
    },
  };
  </script>
  
  <style scoped>
  .father-div {
    width: 30%;
    height: 30%;
    /* filter: blur(10px); */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .father-div .container {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    position: relative;
    z-index: 5;
  }
  .dot1 {
    background: rgba(255,255,255);
    width: 90px;
    height: 90px;
    border-radius: 50%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 5;
  }
  .dot2 {
    background-color: rgba(255,255,255);
    width: 12px;
    height: 12px;
    animation: d2 1.92s; /* 修改动画时长 */
    border-radius: 50%;
    position: absolute;
    left: 24px;
    bottom: 4.8px;
    z-index: 4;
  }
  .dot3 {
    background: rgba(255,255,255);
    animation: d3 1.92s 0.192s; /* 修改动画时长和延迟 */
    width: 9.6px;
    height: 9.6px;
    border-radius: 50%;
    position: absolute;
    left: 24px;
    top: 4.8px;
    z-index: 4;
  }
  .dot4 {
    background: rgba(255,255,255);
    animation: d4 1.92s 0.384s; /* 修改动画时长和延迟 */
    width: 14.4px;
    height: 14.4px;
    border-radius: 50%;
    position: absolute;
    left: 5.76px;
    bottom: 4.8px;
    z-index: 4;
  }
  .dot5 {
    background: rgba(255,255,255);
    animation: d5 1.92s 0.576s; /* 修改动画时长和延迟 */
    width: 17.28px;
    height: 17.28px;
    border-radius: 50%;
    position: absolute;
    left: 5.76px;
    top: 4.8px;
    z-index: 4;
  }
  .dot6 {
    background: rgba(255,255,255);
    animation: d6 1.92s 0.768s; /* 修改动画时长和延迟 */
    width: 7.2px;
    height: 7.2px;
    border-radius: 50%;
    position: absolute;
    left: 18.72px;
    bottom: 1.44px;
    z-index: 4;
  }
  .dot2, .dot3, .dot4, .dot5, .dot6 {
    animation-iteration-count: infinite;
  }
  @keyframes d2 {
    0% {
      left: 48px;
      bottom: 9.6px;
      opacity: 1;
    }
    50% {
      opacity: 1;
    }
    100% {
      left: 102px;
      bottom: -5px;
      opacity: 0;
    }
  }
  @keyframes d3 {
    0% {
      left: 48px;
      top: 9.6px;
      opacity: 1;
    }
    50% {
      opacity: 1;
    }
    100% {
      left: 96px;
      top: 28.8px;
      opacity: 0;
    }
  }
  @keyframes d4 {
    0% {
      left: 9.6px;
      bottom: 9.6px;
      opacity: 1;
    }
    50% {
      opacity: 1;
    }
    100% {
      left: -28.8px;
      bottom: -5px;
      opacity: 0;
    }
  }
  @keyframes d5 {
    0% {
      left: 9.6px;
      top: 9.6px;
      opacity: 1;
    }
    50% {
      opacity: 1;
    }
    100% {
      left: -57.6px;
      top: -9.6px;
      opacity: 0;
    }
  }
  @keyframes d6 {
    0% {
      left: 36px;
      bottom: 2.4px;
      opacity: 1;
    }
    50% {
      opacity: 1;
    }
    100% {
      left: 0px;
      bottom: 150px;
      opacity: 0;
    }
  }
  </style>