<template>
    <div :style="root_st">
        <Title />
        <Introduce />
        <Contact />
    </div>

</template>
<script>
import Title from "./left_index/title.vue"
import Introduce from "./left_index/introduce.vue"
import Contact from "./left_index/contact.vue"
export default{
    data(){
        return{
            root_st:{
                backgroundColor:"green",
                width:"100%",
                display:"flex",
                justifyContent: "center", // 水平居中对齐
                alignItems: "center", // 垂直居中对齐
            }
        }
    },
    components:{
        Title,
        Introduce,
        Contact,
    }
}
</script>