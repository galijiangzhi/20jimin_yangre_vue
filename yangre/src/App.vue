<script>
import Header from "./components/header.vue"
import Service from "./components/service.vue"
import Method from "./components/method.vue"
import Bottom from "./components/bottom.vue"
import Zuozhe from "./components/zuozhe.vue"
export default{
  data(){
    return{
      root_style:{
        height:"100vh",
        width:"100vw",
        display:"flex"
      },
      zuozhe_style:{
        height:"100%",
        width:"300px"
      },
      body_style:{
        height:"100vh",
        width:"100vw",
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
    Zuozhe,
  }
}
</script>

<template>,
<div :style="root_style">
  <div :style="zuozhe_style">
    <Zuozhe />
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
