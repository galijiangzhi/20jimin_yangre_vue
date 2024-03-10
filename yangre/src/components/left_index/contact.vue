<template>
    <div :style="ro_st">
        <button :style="h1_st" @click="toggleDropdown" class="dropdown-toggle">
          <span>联系<br>我们</span>
          <svg :style="svgStyle" t="1709995415343" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5881" width="200" height="200">
            <path d="M915.110634 526.94854c-11.698858-11.698858-30.697002-11.698858-42.39586 0L490.852065 908.711259c-11.698858 11.698858-11.698858 30.697002 0 42.395859s30.697002 11.698858 42.39586 0l381.762718-381.762718c11.798848-11.698858 11.798848-30.697002 0.099991-42.39586z" fill="#515151" p-id="5882"></path><path d="M534.247827 908.811249l-381.962699-381.962699c-11.698858-11.698858-30.697002-11.698858-42.395859 0s-11.698858 30.697002 0 42.39586l381.962699 381.962699c11.698858 11.698858 30.697002 11.698858 42.395859 0s11.698858-30.697002 0-42.39586z" fill="#515151" p-id="5883"></path><path d="M915.110634 72.992872c-11.698858-11.698858-30.697002-11.698858-42.39586 0L490.852065 454.75559c-11.698858 11.698858-11.698858 30.697002 0 42.39586s30.697002 11.698858 42.39586 0l381.762718-381.762718c11.798848-11.698858 11.798848-30.697002 0.099991-42.39586z" fill="#515151" p-id="5884"></path><path d="M534.247827 454.855581l-381.962699-381.962699c-11.698858-11.698858-30.697002-11.698858-42.395859 0s-11.698858 30.697002 0 42.395859l381.962699 381.962699c11.698858 11.698858 30.697002 11.698858 42.395859 0s11.698858-30.697002 0-42.395859z" fill="#515151" p-id="5885">
            </path>
          </svg>
        </button>
        <div :style="root_st" class="contact-icons" v-if="list">
            <img :style="img_st" src="../../../public/电话.png" alt="phone" @mouseover="showInfo('Phone number: 187-9711-2128')" @mouseout="hideInfo" />
            <img :style="img_st" src="../../../public/邮箱.png" alt="email" @mouseover="showInfo('Email: 3105446387@qq.com')" @mouseout="hideInfo" />
            <img :style="img_st" src="../../../public/微信.png" alt="wechat" @mouseover="showInfo('WeChat: wdbayr')" @mouseout="hideInfo" />
            <img :style="img_st" src="../../../public/qq.png" alt="qq" @mouseover="showInfo('QQ: 3105446387')" @mouseout="hideInfo" />
            <img :style="img_st" src="../../../public/邮筒.png" alt="postal" @mouseover="showInfo('Postal code: 810007')" @mouseout="hideInfo" />
        <div v-if="showInfoBox" :style="infoBoxStyle">{{ infoText }}</div>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        ro_st:{
            display:"flex",
            position:"absolute",
            top:"830px",
            width:"390px",
            alignItems: "center" ,
            marginLeft:"1050px",
            marginTop:"20px",
            zIndex: "999"
        },
        root_st: {
          height: "100px",
          width: "390px",
          display: "flex",
          justifyContent: "flex-end",
          alignItems: "center",
          marginRight:"70px",
          alignItems: 'center',

        },
        img_st:{
            height:"30px",
            width:"30px",
            marginRight:"10px",
            transition: "box-shadow 0.3s", // 添加过渡效果
            backgroundColor: "rgba(128, 128, 128, 0.5)",
            borderRadius: "5px" // 添加圆角
        },
        showInfoBox: false,
        infoText: "",
        infoBoxStyle: {
          position: "absolute",
          top: "0px",
          // backgroundColor: "rgba(255, 255, 255, 0.8)",
          padding: "5px",
          borderRadius: "5px"
        },
        list:0
      };
    },
    computed:{
      svgStyle() {
        return {
          transform: this.list ? 'rotate(90deg)' : 'rotate(270deg)',
          transition: 'transform 0.5s'  ,// 添加旋转动画过渡效果
          height:"20px",
          width:"20px",
          marginLeft:"10px",
          border:"1px solid #cccccc",
          borderRadius:"3px",
          
        };
      },
      h1_st(){
        return {
          alignSelf: 'center' ,
          width: "90px",
          height:"90px",
          fontSize:"18px",
          marginLeft:"10px",
          position:"absolute",
          left: this.list? '0px':"-60px",
          top:"0px",
          display:"flex",
          justifyContent: 'center', // 水平居中
          alignItems: 'center',
          backgroundColor:"#ffffff",
          border:"0px",
          borderRadius:"50%",
          boxShadow:null,
          transition:"left 0.5s ease",
          border: this.list ? "1px solid #aaaaaa" : "0px" 
        }
      },
    },
    methods: {
      showInfo(text) {
        this.infoText = text;
        this.showInfoBox = true;
      },
      hideInfo() {
        this.showInfoBox = false;
      },
      toggleDropdown(){
        if (this.$data.list===0){
          this.$data.list=1;
        }else{
          this.$data.list=0;
        }

      }
    }
  };
  </script>
  
  <style scoped>
  .contact-icons img:hover {
    box-shadow: 5px 5px 5px rgba(5, 5, 5, 1);
    border: 2px solid white; /* 添加白色边框 */
  }
  @keyframes d2 {
  0% {
    left: 10px; /* 初始位置 */
    opacity: 1;
  }
  100% {
    left: 30px; /* 向右移动20px */
    opacity: 0;
  }
}
  </style>