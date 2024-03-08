<template>
    <span :style="header_style">最下方作者介绍</span>
</template>
<script>
export default{
    data(){
        return{
            header_style:{
                fontSize:"40px",
                backgroundColor:"green",
                flex:"1"
            }
        }
    }
}
</script>