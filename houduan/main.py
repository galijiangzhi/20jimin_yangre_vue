from flask import Flask, request, send_file
import os
from flask_cors import CORS

app = Flask(__name__)

# 设置上传文件的保存目录
UPLOAD_FOLDER = '/home/baizhen/project/6.jpg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = '/home/baizhen/project/6.jpg'
        file.save(file_path)  # 保存文件
        # 执行脚本
        os.system("/bin/bash /home/baizhen/target_directory/zangyaohua/test.sh")
        return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='192.168.31.100', port=43001)