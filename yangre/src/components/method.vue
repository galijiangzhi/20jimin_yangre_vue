<template>
    <div>
      <span :style="header_style">主要服务逻辑</span>
      <div>
        <input type="file" @change="handleFileUpload">
        <img :src="imageUrl" v-if="imageUrl" alt="上传的图片">
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        header_style: {
          fontSize: "40px",
          backgroundColor: "yellow",
          flex: "1"
        },
        imageUrl: null
      };
    },
    methods: {
        handleFileUpload(event) {
            const formData = new FormData();
            formData.append('file', event.target.files[0]);

            axios.post('http://192.168.31.100:43001/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            responseType: 'arraybuffer' // 设置响应类型为arraybuffer
            })
            .then(response => {
            // 将后端返回的图片数据赋值给imageUrl
            const blob = new Blob([response.data], { type: 'image/jpeg' }); // 创建Blob对象
            const imageUrl = URL.createObjectURL(blob); // 通过URL.createObjectURL将blob转换为URL
            this.imageUrl = imageUrl; // 将URL赋值给组件的imageUrl
            })
            .catch(error => {
            // 处理错误
            console.error('Error uploading file:', error);
            });
        }
        }
  };
  </script>