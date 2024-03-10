<template>
    <div :style="header_style">
        <div :style="test_ts">快速使用指南：<br>&nbsp;&nbsp;&nbsp;&nbsp;请将鼠标移入工作区，点击上传图片按钮，选择您需要进行识别的图片。<br>&nbsp;&nbsp;&nbsp;&nbsp;上传后，系统需要大约30秒的时间来处理并返回识别结果。
        </div>    
    </div>
    <Water />
    <Contact />

</template>
<script>
import Contact from './left_index/contact.vue'
import Water from './bottom/water.vue'
export default{
    data(){
        return{
            header_style:{
                backgroundColor:"rgba(255,255,255,0.3)",
                
            },
            test_ts:{
                fontSize:"20px",
                margin:"20px 20px"
            }
        }
    },
    components:{
        Contact,
        Water,
    }
}
</script>