from flask import Flask, render_template, request
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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        if os.path.exists(file_path):
            os.remove(file_path)  # 删除原文件
        file.save(file_path)  # 保存新文件
        with open('/home/baizhen/a.txt', 'a') as f:
            f.write(file.filename + '\n')

        # 将文件发送到第二个服务器
        send_to_server(file_path, file.filename)

        print('图片已成功转发并处理完成')  # 打印成功信息
        return 'File uploaded, processed and sent back successfully', 200

def send_to_server(file_path, file_name):
    # 建立SSH连接
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('connect.westc.gpuhub.com', port=28184, username='root', password='your_password')

    # 创建SFTP客户端
    sftp_client = ssh_client.open_sftp()

    # 检查远程服务器上是否存在同名文件，如果存在则删除
    remote_path = "/root/chepaijiance/zangyaohua/mydata/train/images/6.jpg"
    try:
        sftp_client.remove(remote_path)
    except FileNotFoundError:
        pass

    # 传输文件
    local_path = file_path
    sftp_client.put(local_path, remote_path)

    # 执行远程命令
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /root/chepaijiance/zangyaohua && bash test.sh')

    # 等待脚本运行完成
    ssh_stdout.channel.recv_exit_status()
    # 传输处理后的文件回到本机
    remote_result_path = '/root/chepaijiance/zangyaohua/runs/detect/exp7/6.jpg'
    if os.path.exists("/home/baizhen/6.jpg"):
        # 如果文件存在，删除它
        os.remove("/home/baizhen/6.jpg")
        print("已删除现有文件")
    local_result_path = '/home/baizhen/6.jpg'

    sftp_client.get(remote_result_path, local_result_path)

    # 关闭连接
    sftp_client.close()
    ssh_client.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=43001, debug=True)
