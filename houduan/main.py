from flask import Flask, request, send_file
import os
from flask_cors import CORS
import time
import shutil
import re

app = Flask(__name__)
CORS(app)  # 启用CORS，允许所有源

# 设置上传文件的保存目录
UPLOAD_FOLDER = '/home/baizhen/project/6.jpg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/lmj', methods=['POST'])
def lmj():
    #lmj
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = '/home/baizhen/project/lmj_ABINet_lock/data/testset/6.jpg'
        file.save(file_path)  # 保存文件
        # 执行脚本
        print("开始执行脚本")
        os.system("python /home/baizhen/project/lmj_ABINet_lock/demo_bz.py")
        print("脚本执行完成")
        test_txt = '/home/baizhen/project/lmj_ABINet_lock/workdir/train-abinet/test.txt'
        with open(test_txt, 'r') as file:
            txt = file.readlines()[-1]
        print(txt)
        txt = re.search(r':\s*(.*)', txt).group(1)
        print(txt)
        return txt

@app.route('/upload', methods=['POST'])
def upload_file():
    #yyrr
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = '/home/baizhen/project/6.jpg'
        file.save(file_path)  # 保存文件

        remove_file = "/home/baizhen/target_directory/zangyaohua/end"
        if os.path.exists(remove_file):
            shutil.rmtree(remove_file)
            print("删除成功")
        # 执行脚本
        print("开始执行脚本")
        os.system("/bin/bash /home/baizhen/target_directory/zangyaohua/test.sh")
        print("脚本执行完成")
        # 发送文件给用户
        file_path = '/home/baizhen/target_directory/zangyaohua/end/6.jpg'
        return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=42001)