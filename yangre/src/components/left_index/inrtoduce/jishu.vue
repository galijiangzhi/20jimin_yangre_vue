<template>
    <div :style="title_st">技术支持</div>
    <div :style="test_st">
        <div :style="te_ti_st">软件：</div>
        <div :style="te_st">&nbsp;&nbsp;OS:debian 12</div>
        <div :style="te_st">&nbsp;&nbsp;Python:3.8.10</div>
        <div :style="te_st">&nbsp;&nbsp;YOLO:V4 </div>
    </div>
    <div :style="test_st">
        <div :style="te_ti_st">硬件：</div>
        <div :style="te_st">&nbsp;&nbsp;cpu_1:e5-2670</div>
        <div :style="te_st">&nbsp;&nbsp;cpu_2:e5-2670</div>
        <div :style="te_st">&nbsp;&nbsp;RAM  :kingston 96GB 10600R</div>
        <div :style="te_st">&nbsp;&nbsp;GPU:RTX 4090</div>
        <div :style="te_st">&nbsp;&nbsp;disk:<br>&nbsp;&nbsp;&nbsp;&nbsp;INTEL SSDSC2BB12 120GB<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raid 0 1.8t<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Seagate ST9600205SS 900G<br>&nbsp;&nbsp;&nbsp;&nbsp;Seagate ST9600205SS 900G<</div>
        <div :style="te_st">&nbsp;&nbsp;阵列卡<br>&nbsp;&nbsp;&nbsp;&nbsp;DELL H310</div>
    </div>
</template>
<script>
export default{
    data(){
        return{
            title_st:{
                fontSize:"25px",
                marginTop:"10px",
                marginBottom:"20px"
            },
            te_ti_st:{
                textAlign:"left",
                width:"300px"
            }
        }
    }
}
</script>