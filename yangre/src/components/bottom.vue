<template>
    <span :style="header_style">页面脚</span>
</template>
<script>
export default{
    data(){
        return{
            header_style:{
                fontSize:"40px",
                backgroundColor:"green",
                flex:"0"
            }
        }
    }
}
</script>