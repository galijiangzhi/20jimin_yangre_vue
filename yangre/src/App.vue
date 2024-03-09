<script>
import Header from "./components/header.vue"
import Service from "./components/service.vue"
import Method from "./components/method.vue"
import Bottom from "./components/bottom.vue"
import Left_index from "./components/left_index.vue"
export default{
  data(){
    return{
      root_style:{
        height:"100%",
        width:"100%",
        display:"flex",
      },
      zuozhe_style:{
        height:"100vh",
        width:"390px",
        backgroundColor:"pink !important"
      },
      body_style:{
        height:"100vh",
        flex:"1",
        display:"flex",
        flexDirection: "column",
        backgroundColor:"green"
      },
      header_style:{
        flex:"1",
        backgroundColor:"blue"
      },
      service_style:{
        flex:"1",
        backgroundColor:"yellow"
      }

    }
  },
  components:{
    Header,
    Service,
    Method,
    Bottom,
    Left_index
  }
}
</script>

<template>
<div :style="root_style">
  <div :style="zuozhe_style">
    <Left_index />
  </div>
  <div :style="body_style">
    <Header />
    <Service />
    <Method />
    <Bottom />
  </div>
</div>
</template>

<style>
</style>
