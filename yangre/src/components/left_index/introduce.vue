<template>
    <div :style="root_st">
      <div :style="div1_st">
        <button :style="but_st" @click="showComponent('Author')" class="button">作者信息</button>
        <button :style="but_st" @click="showComponent('Project')" class="button">项目介绍</button>
        <button :style="but_st" @click="showComponent('Technology')" class="button">生产环境</button>
        <button :style="but_st" @click="showComponent('Prospect')" class="button">未来展望</button>
      </div>
      <div :style="div2_st">
        <component :is="selectedComponent" />
      </div>
    </div>
  </template>
  
  <script>
  import Zuozhe from "./inrtoduce/zuozhe.vue";
  import Xiangmu from "./inrtoduce/xiangmu.vue";
  import Jishu from "./inrtoduce/jishu.vue";
  import Weilai from "./inrtoduce/weilai.vue";
import xiangmu from "./inrtoduce/xiangmu.vue";
  export default {
    data() {
      return {
        root_st: {
          height: "600px",
          height:"100%",
          backgroundColor: "rgba(255,255,255,0.7)",
          display: "flex",
          flexDirection: "column",
          flex:"1"
        },
        div1_st: {
          height: "60px",
          // backgroundColor: "lightblue",
          display:"flex",
        },
        div2_st: {
            flex: "1",
            // backgroundColor: "lightgreen",
            display: "flex",
            flexDirection: "column",  // 将flex-direction设置为column
            justifyContent: "flex-start",  // 垂直向上对齐
            alignItems: "center",
            overflow: 'auto' 
        },
        but_st:{
            flex:"1"
        },
        selectedComponent: xiangmu
      };
    },
    methods: {
      showComponent(option) {
        // 根据选项显示不同的组件
        switch (option) {
          case 'Author':
            this.selectedComponent = Zuozhe; // 使用组件的引用名
            break;
          case 'Project':
            this.selectedComponent = Xiangmu; // 使用组件的引用名
            break;
          case 'Technology':
            this.selectedComponent = Jishu; // 使用组件的引用名
            break;
          case 'Prospect':
            this.selectedComponent = Weilai; // 使用组件的引用名
            break;
          default:
            this.selectedComponent = null;
        }
      }
    },
    components: {
      Zuozhe,
      Xiangmu,
      Jishu,
      Weilai
    }
  };
  </script>
  
  <style>
  .button {
    width: 80px;
    height: 40px;
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.1); /* 半透明的白色 */
    border: none;
    text-align: center;
    line-height: 40px;
    transition: background-color 0.3s; /* 添加背景色过渡效果 */
  }
  
  .button:hover {
    background-color: rgba(255, 255, 255, 1); /* 不透明的白色 */
  }
  </style>