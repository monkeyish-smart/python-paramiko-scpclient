import paramiko  # 用于调用scp命令
from scp import SCPClient
import os

class ScpClient_intface:
    __host = "192.168.0.232"  # 服务器ip地址
    __port = 22  # 端口号
    __username = "root"  # ssh 用户名
    __password = "root"  # 密码
    file_name = "C6SE_project.log" # 操作的文件明
    remote_path = "/A8/"
    local_path = "D:\python_eg"
    def set_scp_server_information(self,host_ip="192.168.0.232",port = 22,username = "root",password = "root"):
        self.__host = host_ip
        self.__port = port
        self.__username = username
        self.__password = password
    def get_file_from_scp_service(self,file_name, remote_path="/A8/",  local_path="D:\python_eg"):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(self.__host, self.__port, self.__username, self.__password)
        scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
        # local_path = file_path + "\\" + img_name
        file_path_lo = local_path
        file_path_re = remote_path + '/' + file_name
        #file_path_re = remote_path

        print(file_path_lo)
        print(file_path_re)
        try:

           #  print(local_path)
           # scpclient.put(localpath, remotepath)  # 上传到服务器指定文件
            scpclient.get(file_path_re, file_path_lo)  # 从服务器中获取文件
        except FileNotFoundError as e:
            print(e)
            print("system could not find the specified file" + local_path)
            result = "system could not find the specified file" + local_path
        else:
            print("File downloaded successfully")
            result ="File downloaded successfully"
        ssh_client.close()
        return result
    def put_file_to_scp_service(self,file_name, remote_path="/A8/",  local_path="D:\python_eg"):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(self.__host, self.__port, self.__username, self.__password)
        scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
       # local_path = file_path + "\\" + img_name
        file_path_lo = local_path + '/' + file_name
        file_path_re = remote_path

        print(file_path_lo)
        print(file_path_re)
        try:
           scpclient.put(file_path_lo, file_path_re)  # 上传到服务器指定文件
           #scpclient.get(file_path_re, file_path_lo)  # 从服务器中获取文件
        except FileNotFoundError as e:
            print(e)
            print("system could not find the specified file" + local_path)
            result = "system could not find the specified file" + local_path
        else:
            print("文件上传成功")
            result = "File uploaded successfully"
        ssh_client.close()
        return result
if __name__ == "__main__":
    #upload_img("C6SE")
    #print(os.getcwd())
    scp_cc = ScpClient_intface()
    scp_cc.set_scp_server_information()
    scp_cc.get_file_from_scp_service("C6SE_project.log",local_path=os.getcwd() )
    #scp_cc.put_file_to_scp_service("ScpClient_intface.py",local_path=os.getcwd())