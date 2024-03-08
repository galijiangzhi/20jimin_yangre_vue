from flask import Flask,render_template,request
import os
import paramiko

app = Flask(__name__)

# 设置SSH连接的参数
UPLOAD_FOLDER = '/home/baizhen'  # 替换为你想要保存上传图片的目录
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        with open('/home/baizhen/a.txt', 'a') as f:
            f.write(file.filename + '\n')
        return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=43001,debug=True)