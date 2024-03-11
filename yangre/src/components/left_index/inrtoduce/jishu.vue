<template>
    <div :style="title_st">生产环境</div>
    <div :style="test_st">
        <div :style="te_ti_st">软件环境</div>
        <div :style="telist_st">
            <div :style="te_st">OS:debian 12</div>
            <div :style="te_st">Python:3.8.10</div>
            <div :style="te_st">YOLO:V5 </div>
        </div>
        
    </div>
    <div :style="test_st">
        <div :style="te_ti_st">硬件环境：</div>
        <div :style="telist_st">
            <div :style="te_st">CPU_1:Intel Xeon E5-2670</div>
            <div :style="te_st">CPU_2:Intel Xeon E5-2670</div>
            <div :style="te_st">RAM:kingston 96GB 10600R</div>
            <div :style="te_st">GPU:RTX 4090 24GB</div>
            <div :style="te_st">DISK:
                <div :style="two_te_st">
                    INTEL SSDSC2BB12 120GB
                    <div :style="three_te_st">RAID_0 1.8TB
                        <div :style="four">
                            <div>Seagate ST9600205SS 900GB</div>
                            <div>Seagate ST9600205SS 900GB</div>
                        </div>
                    </div>
                </div>
            </div>
            <div :style="te_st">阵列卡:DELL H310</div>
        </div>
       
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
                width:"300px",
            },
            telist_st:{
                textIndent: "20px"
            },
            two_te_st:{
                textIndent: "40px"
            },
            four:{
                textIndent:"60px"
            }
        }
    }
}
</script>