<template>
    <span :style="header_style">
        <h1 :style="h1_st">藏 药 花 识 别 平 台</h1>
        <h1 :style="h2_st">བོད་སྨན་མེ་ཏོག་དབྱེ་འབྱེད་མ་ལག</h1>
    </span>
</template>
<script>
export default{
    data(){
        return{
            h1_st:{
                fontSize:"40px",
                textAlign: "center",
                margin: "0"  // 确保标题之间没有间距
            },
            h2_st:{
                fontSize:"40px",
                textAlign: "center",
                margin: "0"  // 确保标题之间没有间距
            },
            header_style:{
                fontSize:"40px",
                backgroundColor:"rgba(255,255,255,0.6)",
                height:"200px", /* 增加高度，以容纳两个标题 */
                display:"flex",
                flexDirection: "column", /* 设置垂直排列 */
                justifyContent: "center",  // 垂直居中
                alignItems: "center"  // 水平居中
            }
        }
    }
}
</script>