#!/user/bin/python
# -*- coding:utf-8 -*-
#client  客户端
# import socket
# while True:
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     #连接服务器
#     sock.connect(('127.0.0.1',8888))
#     a = input('请输入请求')
#     if a =='exit':
#         #断开连接
#         sock.close()
#         break
#     else:
#         # send发送请求
#         sock.send(a.encode('utf-8'))
#         # 接收数据
#         msg = sock.recv(1024)
#         print(msg.decode('utf-8'))



#udp 客户端
import socket
while True:
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #直接发送请求
    host=('127.0.0.1',8888)
    a=input('请输入请求:')
    if a=='exit':
        break
    else:
        sock.sendto(a.encode('utf-8'),host)
        #接收数据
        msg=sock.recv(1024)
        print(msg.decode('utf-8'))
        sock.close()