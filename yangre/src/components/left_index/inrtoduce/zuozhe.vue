<template>
    <div>
      <div class="image-container">
        <img :style="header_st"
          src="../../../../public/a.jpg" 
          alt="圆形图片" 
          class="circle-image" 
          @mouseover="zoomIn" 
          @mouseleave="zoomOut" 
          style="width: 80px; height: 80px;"
        />
      </div>
      <div class="description">
        <p>21人工智能 白稹 2021090116 <br> 指导老师:唐明虎 <br>主要成就: </p>
        <p>西宁市第91李白 1235场54胜率 <br>西宁市第16兰陵王 560场58胜率 <br>沈阳市第64姜子牙 228场54胜率 <br>沈阳市第87刘邦 389场59胜率 <br>西宁市第九94盘古 <br>城东区第16赵云 384长57胜率 <br>城东区第21项羽 <br>城东区第26刘备 <br>城东区第32姬小满 <br>城东区第39司马懿 281场58胜率<br>剑网三剑纯竞技场9段 <br>剑网三2023年好师父 <br>英雄联盟男爵领域黄金1 <br>英雄联盟“绝对主坦”称号 <br>鹅鸭杀50级选手 <br>金铲铲铂金一</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data(){
        return{
            header_st:{
            },
        }
    },
    methods: {
      zoomIn(event) {
        event.target.style.transform = "scale(1.2)";
      },
      zoomOut(event) {
        event.target.style.transform = "scale(1)";
      }
    }
  };
  </script>
  
  <style>
  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 40px;
  }
  
  .circle-image {
    border-radius: 50%;
    transition: transform 0.3s; /* 添加缩放效果的过渡 */
  }
  
  .description {
    text-align: center;
    margin-top: 10px;
    flex:1;
  }

  .description p:nth-child(2) {
  text-align: left;
}
  </style>