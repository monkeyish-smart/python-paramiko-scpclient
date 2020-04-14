#!/usr/bin/python3
#-*- encoding=UTF-8 -*-
import tkinter as tk
import ScpClient_intface as sci
import os
def scp_put_file():
    print(En_host.get(),En_port.get(),En_username.get(),En_password.get(),En_file_name_put.get(),En_remote_path_put.get())
    if En_username.get() == "" or En_password.get() == "":
        scp_put = sci.ScpClient_intface()
        scp_put.set_scp_server_information( host_ip=En_host.get(), port = En_port.get())
        result = scp_put.put_file_to_scp_service(En_file_name_put.get(), remote_path=En_remote_path_put.get(),local_path=os.getcwd())
    else:
        scp_put = sci.ScpClient_intface()
        scp_put.set_scp_server_information( host_ip=En_host.get(), port = En_port.get(), username = En_username.get(), password = En_password.get())
        result = scp_put.put_file_to_scp_service(En_file_name_put.get(), remote_path=En_remote_path_put.get(),local_path=os.getcwd())
    root1 = tk.Tk()
    root1.title('result')
    root1.geometry('200x100')  # 这里的乘是小x
    tk.Label(root1, text=result, fg='blue', font=('Arial', 10)).pack()
    #scp_put = sci.ScpClient_intface()
    #scp_put.set_scp_server_information()
    #scp_put.get_file_from_scp_service("C6SE_project.log", local_path=os.getcwd())
    #scp_put.put_file_to_scp_service("ScpClient_intface.py", local_path=os.getcwd())
def scp_get_file():
    print(En_host.get(), En_port.get(), En_username.get(), En_password.get(), En_file_name_get.get(), En_remote_path_get.get())
    if En_username.get() == "" or En_password.get() == "":
        scp_get = sci.ScpClient_intface()
        scp_get.set_scp_server_information(host_ip=En_host.get(), port=En_port.get())
        result = scp_get.get_file_from_scp_service(En_file_name_get.get(), remote_path=En_remote_path_get.get(), local_path=os.getcwd())
    else:
        scp_get = sci.ScpClient_intface()
        scp_get.set_scp_server_information(host_ip=En_host.get(), port=En_port.get(), username=En_username.get(),password=En_password.get())
        result = scp_get.get_file_from_scp_service(En_file_name_get.get(), remote_path=En_remote_path_get.get(),local_path=os.getcwd())
    root1 = tk.Tk()
    root1.title('result')
    root1.geometry('200x100')  # 这里的乘是小x
    tk.Label(root1, text=result, fg='blue', font=('Arial', 10)).pack()
def about():
    root1 = tk.Tk()
    root1.title('about')
    root1.geometry('200x100')  # 这里的乘是小x
    tk.Label(root1, text='versions 1.0', fg='blue', font=('Arial', 10)).pack()
    tk.Label(root1, text='zhanyongli@xcharge.com', fg='blue', font=('Arial', 10)).pack()
if __name__ == "__main__":
    # 第1步，实例化object，建立窗口window
    root = tk.Tk()   # 创建窗口对象的背景色
    # 第2步，给窗口的可视化起名字
    root.title('SCP client for file operation')
    # 第3步，设定窗口的大小(长 * 宽)
    root.geometry('520x220')  # 这里的乘是小x
    tk.Label(root, text='Host name(ip)', font=('Arial', 10)).place(x=10, y=10)
    tk.Label(root, text='port', font=('Arial', 10)).place(x=150, y=10)
    tk.Label(root, text='User name:', font=('Arial', 10)).place(x=250, y=10)
    tk.Label(root, text='Password:', font=('Arial', 10)).place(x=400, y=10)
    # 第4步，在图形界面上设定输入框控件entry并放置控件
    En_host = tk.StringVar()
    En_port = tk.StringVar()
    En_username = tk.StringVar()
    En_password = tk.StringVar()
    En_file_name_get = tk.StringVar()
    En_remote_path_get = tk.StringVar()
    En_file_name_put = tk.StringVar()
    En_remote_path_put = tk.StringVar()
    tk.Entry(root, textvariable = En_host,show=None,  font=('Arial', 10)).place(x=10, y=30,width= 120) # 显示成密文形式
    tk.Entry(root, textvariable = En_port, show=None, font=('Arial', 10)).place(x=150, y=30,width= 50) # 显示成明文形式
    tk.Entry(root, textvariable = En_username, show=None,  font=('Arial', 10)).place(x=250, y=30,width= 100)  # 显示成密文形式
    tk.Entry(root, textvariable = En_password, show='*', font=('Arial', 10)).place(x=400, y=30,width= 100)  # 显示成明文形式
    En_port.set("22")
    tk.Label(root, text='Remote Directory:', font=('Arial', 10)).place(x=10, y=70)
    tk.Label(root, text='File name:', font=('Arial', 10)).place(x=10, y=100)
    tk.Label(root, text='Remote Directory:', font=('Arial', 10)).place(x=10, y=150)
    tk.Label(root, text='File name:', font=('Arial', 10)).place(x=10, y=180)

    tk.Entry(root, textvariable = En_remote_path_put, show=None,  font=('Arial', 10)).place(x=150, y=70,width= 300) # 显示成密文形式
    tk.Entry(root, textvariable = En_file_name_put, show=None, font=('Arial', 10)).place(x=150, y=100,width= 300) # 显示成明文形式
    tk.Entry(root, textvariable = En_remote_path_get, show=None,  font=('Arial', 10)).place(x=150, y=150,width= 300)  # 显示成密文形式
    tk.Entry(root, textvariable = En_file_name_get, show=None, font=('Arial', 10)).place(x=150, y=180,width= 300)  # 显示成明文形式

    tk.Button(root, text='put', anchor='c', width=6, height=1, command=scp_put_file).place(x=450, y=80,height=50,width= 50)
    tk.Button(root, text='get', anchor='c', width=6, height=1, command=scp_get_file).place(x=450, y=150,height=50,width= 50)

    menubar = tk.Menu(root)
    #aaa= sci.ScpClient_intface()
    #创建下拉菜单File，然后将其加入到顶级的菜单栏中
    #filemenu = tk.Menu(menubar,tearoff=0)
    #filemenu.add_command(label="Open", command=hello)
    #filemenu.add_command(label="Save", command=hello)
    #filemenu.add_separator()
    #ilemenu.add_command(label="Exit", command=root.quit)
    #menubar.add_cascade(label="File", menu=filemenu)

    #创建另一个下拉菜单Edit
    #editmenu = tk.Menu(menubar, tearoff=0)
    #editmenu.add_command(label="Cut", command=hello)
    #editmenu.add_command(label="Copy", command=hello)
    #editmenu.add_command(label="Paste", command=hello)
    #menubar.add_cascade(label="Edit",menu=editmenu)
    #创建下拉菜单Help
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    #显示菜单
    root.config(menu=menubar)
    # 进入消息循环
    # tk.mainloop()
    root.mainloop()