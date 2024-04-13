<template>
  <div :style="root_st" @mouseenter="showInSt" @mouseleave="hideInSt">
    <div :style="bott_st" ref="bottSt">
      <div :style="[in_st, in_st_visible]" @click="triggerFileInput" @mouseenter="inin" @mouseleave="inout">
        <input ref="fileInput" type="file" @change="handleFileUpload" style="display: none;">
        <span>上传文件</span>
      </div>
      <div :style="[do_st, do_st_visible]" @mouseenter="doin" @mouseleave="doout" @click="saveImage">
        <span>保存文件</span>
      </div>
    </div>
    
    <div :style="img_div_st">
      <Xuanzhuan v-if="showComponent" size="60" borderWidth="6" />
      <img :style="img_st" :src="imageUrl" v-if="imageUrl" alt="上传的图片">
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import Xuanzhuan from './method/xuanzhuan.vue'
export default {
  data(){
    return {
      in_st_visible: {
        opacity: 0,
        transform: "translateY(50px)",
        transition: "opacity 0.5s, transform 0.5s"
      },
      do_st_visible: {
        opacity: 0,
        transform: "translateY(50px)",
        transition: "opacity 0.5s, transform 0.5s",
      },
      root_st: {
        width: "100%",
        height: "750px",
        backgroundColor: "rgba(255,255,255,0)",
        position: "relative",
      },
      bott_st:{
        position: "relative",
        top:"85%",
        width:"100%",
        height:"100px",
        // backgroundColor:"pink",
        display:"flex",
        justifyContent: "space-around",
        paddingLeft:"300px", /* 左侧内侧面的禁区 */
        paddingRight:"300px", /* 右侧内侧面的禁区 */
        boxSizing: "border-box",
        zIndex: 9999
      },
      in_st: {
        width: "200px",
        height: "55px",
        backgroundColor: "rgba(255,255,255,0.7)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        cursor: "pointer",
        boxShadowStyle:'none'
        // position: "absolute",
      },
      do_st: {
        width: "200px",
        height: "55px",
        backgroundColor: "rgba(255,255,255,0.7)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        cursor: "pointer",
        boxShadowStyle:'none'
        // position: "absolute",
      },
      img_div_st:{
        width:"100%",
        height:"100%",
        position: "absolute",
        // backgroundColor:"red",,
        left:"0px",
        top:"0px",
        display:"flex",
        justifyContent: "center", // 将子元素水平居中
        alignItems: "center" // 将子元素垂直居中
      },
      img_st:{
        maxWidth: "90%",
        maxHeight: "90%",
        border: "5px solid pink" // 添加粉色外边框
      },
      showComponent:0,
      imageUrl: null,
      imageBlob: null,
    }
  },
  components:{
    Xuanzhuan,
  },
  methods: {
    saveImage() {
      if (this.imageBlob) {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(this.imageBlob);
        link.download = 'image.jpg';
        link.click();
      } else {
        // 如果没有图片Blob，给出提示或者执行其他操作
        console.error('No image to save');
      }
    },
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    showInSt() {
      this.in_st_visible.opacity = 1;
      this.in_st_visible.transform = "translateY(0)";
      this.do_st_visible.opacity = 1;
      this.do_st_visible.transform = "translateY(0)";
    },
    hideInSt() {
      this.in_st_visible.opacity = 0;
      this.in_st_visible.transform = "translateY(50px)";
      this.do_st_visible.opacity = 0;
      this.do_st_visible.transform = "translateY(50px)";
    }
  }
};
</script>

<style>
.bott-st {
  position: relative;
  width: 500px;
  height: 200px;
  /* background-color: pink; */
}
.in-st {
  width: 100px;
  height: 100px;
  /* background-color: red; */
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  position: absolute;
  bottom: 20px;
  left: 120px;
}
.do-st {
  width: 100px;
  height: 100px;
  /* background-color: red; */
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  position: absolute;
  bottom: 20px;
  left: 220px;
}

</style>