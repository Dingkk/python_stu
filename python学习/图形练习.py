#!/user/bin/python
# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
def closewindow():
    #设置提示信息
    messagebox.showinfo(title='哈哈哈，关不掉',message='就是关不掉')
    # 关闭窗口
    window.destroy()
    return
def love():
    #创建一个顶级窗口，依赖原始窗口存在
    # love=Toplevel(window)

    # love.geometry('220x180+550+300')
    messagebox.showinfo(title='太好了',message='回答正确')
    label.grid(row=1, columnspan=1, sticky=W)
    # love.mainloop()
def nolove():
    nolove=Toplevel(window)
    nolove.title('好好想想哦')
    nolove.geometry('240x180+530+300')
    label = Label(nolove, text='回答错误', font=("微软雅黑", 20))
    label.grid(row=1, columnspan=1, sticky=W)
    nolove.mainloop()

#创建一个窗口
window=Tk()
#命名窗口的标题
window.title("Hello 小姐姐")
#设置窗口的大小
window.geometry('380x360+450+200')
#设置窗口的位置
# window.geometry(+0+0)
#当用户关闭窗口时触发
window.protocol('WM_DELETE_WINDOW',closewindow)
#添加一个文本标签(控件）
label=Label(window,text='hsadf',font=("微软雅黑",20))
#显示标签(行，列，以什么对齐，E,S,W,N）
label.grid(row=1,columnspan=1,sticky=W)
#添加图片控件
# imag=PhotoImage(file='cc.png')
# image=Label(window,image=imag)
# image.grid(row=2,columnspan=2)

#第二种添加（pillow，就第5，6行）
photo=Image.open('cc.png')
phot=ImageTk.PhotoImage(photo)
pho=Label(window,image=phot)
#显示数据
pho.grid(row=2,columnspan=2)

botten=Button(window,text='同意',width=7,height=2,command=love)
botten.grid(row=3,column=0,sticky=W)
botten=Button(window,text='不同意',width=7,height=2,command=nolove)
botten.grid(row=3,column=1,sticky=E)
#显示窗口
window.mainloop()
