#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
import tkinter.font as tkf

from tkinter import *
from tkinter import scrolledtext
import tkinter.filedialog as tkdg
from Class_Part_Speech_HMM import *



#点击翻译函数
def runsentence(miaowen):
    HMM = miaowenHMM()
    # print("请输入语句：")
    miaowen = miaowen.replace('\n','')
    test_str_input = miaowen

    test_str_f = jieba.cut(test_str_input, HMM=True)

    L = ' '.join(test_str_f)
    Test = L.split(' ')

    prob, pos_list = HMM.Part_of_Speech(Test)

    #print('原始语句为：' + HMM.getIntputData())
    #print('切割后的语句为：' + str(HMM.getPartData()))
    #print('词性标注后为：' + str(HMM.getPartNominalInformation()))
    #print(pos_list)

    pos_list = pos_list.split(' ')

    comb = []
    for i in range(len(Test)):
        comb.append(Test[i] + ' (' + pos_list[i] + ')')

    return comb,miaowen

def reg():
    global baseFrame
    miaowen=e1.get("0.0", "end")
    #这里的变量miaowen就是文本框中输入的内容，加算法传入miaowen

    comb, miaowen = runsentence(miaowen)
    #lb3["text"] = '切割后的语句为：' + str(Test)
    #lb4["text"] = '词性标注后为：' + str(pos_list)
    #lb2["text"] = '原始语句为：' + miaowen
    chu1.config(state=NORMAL)
    chu1.delete(1.0,END)
    chu1.insert(INSERT,str(comb))
    chu1.config(state=DISABLED)


def pop(event):
    menubar2.post(event.x_root,event.y_root)

def copy():
    e1.event_generate("<<Copy>>")
    chu1.event_generate("<<Copy>>")
def cut():
    e1.event_generate("<<Cut>>")
    chu1.event_generate("<<Cut>>")
def paste():
    e1.event_generate("<<Paste>>")


#版本信息
def makelabel():
    #弹出版本信息
    global baseFrame
    baseFramesee=tkinter.Toplevel()
    baseFramesee.geometry("373x425+500+150")
    baseFramesee.wm_title("版本信息")
    baseFramesee.resizable(0,0)

    windVer = scrolledtext.ScrolledText(baseFramesee, width=50, height=30)
    windVer.grid(row=0,column=0, sticky=E+W)

    btnVer = Button(baseFramesee, text="返回", command=lambda:baseFramesee.destroy())
    btnVer.grid(row=1,column=0, sticky=E+W)

    with open("VerInformation_MiaoWen.txt","r") as fp:
        windVer.insert(INSERT, str( fp.read() ) )
        windVer.config(state=DISABLED)


#文件浏览
def openF():
    def brow(brsw,shpa):
        global pathF
        brsw.wm_attributes("-topmost",0)
        pathF=tkdg.askopenfilename(filetypes={("Text file", "*.txt*")})
        shpa.delete(END)
        shpa.insert(INSERT,str(pathF))
        brsw.wm_attributes("-topmost",1)

    browseWindow=tkinter.Toplevel()
    browseWindow.geometry("400x62+450+300")
    browseWindow.wm_title("路径设置")
    browseWindow.resizable(0,0)

    showPath=Entry(browseWindow)
    showPath.grid(row=0,column=0,columnspan=5,ipadx=100,sticky=E+W)

    findF=Button(browseWindow, text="更换目录", command=lambda:brow(browseWindow,showPath))
    findF.grid(row=0,column=6)

    Yeah=Button(browseWindow, text="确定", command=lambda:copyIn(browseWindow))
    Yeah.grid(row=1,column=0,columnspan=7,padx=0, sticky=E+W)

    brow(browseWindow,showPath)

def copyIn(dety):
    global pathF
    print(pathF)
    dety.destroy()
    if pathF != "":
        with open(pathF,'r',encoding="utf-16") as fp:
            e1.insert(INSERT,str( fp.read() ))


#文件保存
def saveF():
    global pathF
    sav = chu1.get(1.0, END)
    if sav != "\n":
        pathF = tkdg.asksaveasfilename()
        with open(pathF, "w", encoding="utf-16") as fp:
            fp.write(sav)
    else:
        warning("文本框为空!")

def warning(warn):
    winWar = tkinter.Toplevel()
    winWar.geometry("250x130+525+240")
    winWar.wm_title("提示")
    winWar.wm_attributes("-topmost",1)
    winWar.resizable(0,0)

    textWar=tkinter.Label(winWar, text=warn, font=tkf.Font(family="SimHei",size = 12))
    textWar.pack(expand="yes")

    btnEnsu=tkinter.Button(winWar, text="确定", width=15,height=1, command=lambda:winWar.destroy())
    btnEnsu.pack(expand="yes")




if __name__ == '__main__':
    baseFrame=tkinter.Tk()
    baseFrame.geometry("700x500+310+80")
    baseFrame.resizable(0,0)

    #标题
    baseFrame.wm_title("方块苗文词性标注器1.50")

    #路径
    pathF=StringVar()

    #菜单
    menubar1=tkinter.Menu(baseFrame)

    fmenu=tkinter.Menu(menubar1, tearoff=0)
    fmenu.add_command(label="Open", command=openF)
    fmenu.add_command(label="Save", command=saveF)

    emenu=tkinter.Menu(menubar1, tearoff=0)
    emenu.add_command(label="Copy", command=copy)
    emenu.add_command(label="Cut", command=cut)
    emenu.add_command(label="Paste", command=paste)

    menubar1.add_cascade(label='File', menu=fmenu)
    menubar1.add_cascade(label='Edit', menu=emenu)
    menubar1.add_cascade(label='About', command=makelabel)

    #右键点击功能
    menubar2=tkinter.Menu(baseFrame, tearoff=0)
    menubar2.add_command(label="复制", command=copy)
    menubar2.add_command(label="剪切", command=cut)
    menubar2.add_command(label="粘贴", command=paste)
    menubar2.add_command(label='版本信息',command=makelabel)

    #背景图片
    img = PhotoImage(file="bg3.gif")
    bgr = Canvas(baseFrame, width=700,height=500,bd=0, highlightthickness=0)
    bgr.create_image(300,120, image=img)
    bgr.pack()

    #显示
    lb1=tkinter.Label(baseFrame, text="         请输入要标注的文本:         ", fg="white", bg="black")
    lb1.pack()
    chu1_lb=tkinter.Label(baseFrame, text="         切割后的语句为：         ", fg="white", bg="black")
    chu1_lb.pack()
    tip1=tkinter.Label(baseFrame, text="n/名词 np/人名 ns/地名 ni/机构名 nz/其它专名\nm/数词 q/量词 mq/数量词 t/时间词 f/方位词   \ns/处所词 v/动词 vm/能愿动词 vd/趋向动词      \na/形容词 d/副词 h/前接成分 k/后接成分 i/习语\nj/简称 r/代词 c/连词 p/介词 u/助词 y/语气助词\ne/叹词 o/拟声词 g/语素 w/标点 x/其它           ", fg="white", bg="black")

    bgr.create_window(66,15, width=120,height=20, window=lb1)
    bgr.create_window(57,255, width=95,height=20, window=chu1_lb)
    bgr.create_window(505,400, width=300,height=120, window=tip1)


    #输入框
    e1 = scrolledtext.ScrolledText(baseFrame, width=70, height=15, fg="black", bg="LightGrey")  #滚动文本框（宽，高（这里的高应该是以行数为单位）
    e1.pack()
    #空白显示
    lb11=tkinter.Label(baseFrame,text="         ")
    lb11.pack()
    #按钮点击及点击结果
    btn=tkinter.Button(baseFrame, text="开始进行标注",command=reg, font=tkf.Font(family="SimHei",size = 12), fg="DarkOrange", bg="black")
    btn.pack()

    bgr.create_window(160,120, width=300,height=190, window=e1)
    bgr.create_window(505,305, width=260,height=50, window=btn)

    
    #输出框

    chu1=scrolledtext.ScrolledText(baseFrame, width=70, height=15, fg="black", bg="LightGrey")  #滚动文本框（宽，高（这里的高应该是以行数为单位）
    chu1.config(state=DISABLED)
    chu1.pack()
    #chu1.insert(INSERT,miaowen)


    bgr.create_window(160,370, width=300,height=210, window=chu1)


    #汇总，消息循环
    baseFrame['menu']=menubar1
    baseFrame.bind("<Button-3>",pop)
    baseFrame.mainloop()