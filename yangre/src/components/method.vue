<template>
    <span :style="header_style">主要服务逻辑</span>
    <div>
        <input type="file" @change="uploadImage">
    </div>
</template>

<script>
export default{
    data(){
        return{
            header_style:{
                fontSize:"40px",
                backgroundColor:"yellow",
                flex:"1"
            }
        }
    },
    methods: {
    uploadImage(event) {
      const formData = new FormData();
      formData.append('file', event.target.files[0]);

      fetch('http://192.168.31.100:43001/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        // Handle response
      })
      .catch(error => {
        // Handle error
      });
    }
  }
}
</script>