<template>
    <div>
      <div class="image-container">
        <img :style="header_st"
          src="../../../../public/a.jpg" 
          class="circle-image" 
          @mouseover="zoomIn" 
          @mouseleave="zoomOut" 
          style="width: 80px; height: 80px;"
        />
      </div>
      <div class="description">
        <p>21人计民 杨热 2021090116 <br> 指导老师:唐明虎 <br>青海民族大学计算机学院<br>藏文信息处理研究院 实验员<br>主要成就: </p>
        <!-- <p>西宁市第91李白 1235场54胜率 <br>西宁市第16兰陵王 560场58胜率 <br>沈阳市第64姜子牙 228场54胜率 <br>沈阳市第87刘邦 389场59胜率 <br>西宁市第九94盘古 <br>城东区第16赵云 384长57胜率 <br>城东区第21项羽 <br>城东区第26刘备 <br>城东区第32姬小满 <br>城东区第39司马懿 281场58胜率<br>剑网三剑纯竞技场9段 <br>剑网三2023年好师父 <br>英雄联盟男爵领域黄金1 <br>英雄联盟“绝对主坦”称号 <br>鹅鸭杀50级选手 <br>金铲铲铂金一</p> -->
        <p :style="p2_st">2023 高教社杯数学建模赛区（省级）一等奖<br>2023 年第二十届五一数学建模竞赛荣获“二等奖<br>2022 年青海民族大学首届数学建模竞赛荣获“一等奖”<br>2023 年第九届互联网+校赛荣获“一等奖、省赛荣获“金奖”、国赛荣获“铜奖”。<br>2023 年青海民族大学计算机学院荣获“励志奖学金”<br>2023 年青海省校园艺术节省级展演系列舞蹈专场荣获“二等奖”<br>2023 届毕业生音乐会中表现突出 ，荣获“最佳表演者”<br>2021 年青海民族大学计算机学院“度田桎运动会”活动中，荣获“优秀表演者”<br>2022 年度青海民族大学计算机学院“忠实践行三十大，踔厉百发谱华章”主起领讲比赛中荣获“优秀奖”</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data(){
        return{
            p2_st:{
              fontSize:"18px",
              marginLeft:"10px",
              marginRight:"15px"
            }
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
    margin-top: 20px;
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