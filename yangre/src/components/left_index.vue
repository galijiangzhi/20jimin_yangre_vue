<template>
    <div :style="root_st">
        <div :style="title_st">
            <Title />
        </div>
        <div :style="introduce_st">
            <Introduce />
        </div>

    </div>

</template>
<script>
import Title from "./left_index/title.vue"
import Introduce from "./left_index/introduce.vue,"
export default{
    data(){
        return{
            root_st:{
                backgroundColor:"rgba(255,255,255,0.5)",
                width:"100%",
                height:"100%",
                display:"flex",
                flexDirection: "column", // 从上到下排列
                justifyContent: "center", // 水平居中对齐
                alignItems: "center" ,// 垂直居中对齐,
                // backgroundColor:"pink"
            },
            title_st:{
                height:"250px",
                width:"100%",
                // backgroundColor:"green",
                display:"flex",
                justifyContent: "center", // 横向居中对齐
                alignItems: "center" // 垂直居中对齐
            },
            introduce_st:{
                width:"100%",
                flex:"1",
                overflow: 'auto'
                // backgroundColor:"yellow"
            }
        }
    },
    components:{
        Title,
        Introduce,
    }
}
</script>