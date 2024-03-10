<template>
    <div class="spinner-container">
      <div class="spinner"></div>
      <p>分析时间大约需要20秒，请耐心等候</p>
    </div>
  </template>
  
  <style scoped>
  .spinner-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh; /* 设置高度为视口高度，使内容垂直居中 */
  }
  
  .spinner {
    border: 6px solid rgba(0, 0, 0, 0.1); /* 调整边框宽度 */
    border-top: 6px solid #3498db; /* 调整顶部边框宽度和颜色 */
    border-radius: 50%;
    width: 60px; /* 设置宽度为60px */
    height: 60px; /* 设置高度为60px */
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  </style>