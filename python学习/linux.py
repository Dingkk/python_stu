#!/user/bin/python
# -*- encoding:utf-8 -*-
import paramiko
with paramiko.SSHClient() as ssh111:
    ssh111.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh111.connect(hostname='192.168.0.101',
                   port=22,
                   username='root',
                   password='123456')
    while True:
        m=input('请输入linux命令:')
        if m=='exit':
            break
        else:
            a,b,c=ssh111.exec_command(m)
            print(b.read().decode())
