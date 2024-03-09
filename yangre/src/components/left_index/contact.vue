<template>
    <div :style="h1_st">联系我们</div>
    <div :style="root_st" class="contact-icons">
      <img :style="img_st" src="../../../public/电话.png" alt="phone" @mouseover="showInfo('Phone number: 132-4367-2048')" @mouseout="hideInfo" />
      <img :style="img_st" src="../../../public/邮箱.png" alt="email" @mouseover="showInfo('Email: galijiangzhi@163.com')" @mouseout="hideInfo" />
      <img :style="img_st" src="../../../public/微信.png" alt="wechat" @mouseover="showInfo('WeChat: PLBRDWYYJZSXYSDN')" @mouseout="hideInfo" />
      <img :style="img_st" src="../../../public/qq.png" alt="qq" @mouseover="showInfo('QQ: 2981563487')" @mouseout="hideInfo" />
      <img :style="img_st" src="../../../public/邮筒.png" alt="postal" @mouseover="showInfo('Postal code: 810007')" @mouseout="hideInfo" />
      <div v-if="showInfoBox" :style="infoBoxStyle">{{ infoText }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        h1_st:{
            position: "absolute",
            height: "100px",
            width: "390px",
            left:"20px",
            top: "965px",
            fontSize:"30px"
        },
        root_st: {
          position: "absolute",
          height: "100px",
          width: "390px",
          top: "940px",
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center"
        },
        img_st:{
            height:"40px",
            width:"40px",
            marginRight:"10px",
            transition: "box-shadow 0.3s", // 添加过渡效果
            backgroundColor: "rgba(128, 128, 128, 0.5)",
            borderRadius: "5px" // 添加圆角
        },
        showInfoBox: false,
        infoText: "",
        infoBoxStyle: {
          position: "absolute",
          top: "80px",
          backgroundColor: "rgba(255, 255, 255, 0.8)",
          padding: "5px",
          borderRadius: "5px"
        }
      };
    },
    methods: {
      showInfo(text) {
        this.infoText = text;
        this.showInfoBox = true;
      },
      hideInfo() {
        this.showInfoBox = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .contact-icons img:hover {
    box-shadow: 5px 5px 5px rgba(5, 5, 5, 1);
    border: 2px solid white; /* 添加白色边框 */
  }
  </style>