#导入资源
from lrsclasses import *
from wxfunctions import *
import random
import time
#创建变量
Waiting=[]
#设置参数
Langren.number=2
Nvwu.number=1
Yuyanjia.number=1
Shouwei.number=1
Pingmin.number=3
Game=[]
Table={}
#临时参数
dengdailangren=False
dengdaishouwei=False
dengdainvwu=False
dengdaiyuyanjia=False
#登陆微信(Itchat部分)
wx.login()

#开始游戏
def startgame():
    temp=[]
    for x in range(Langren.number):
        temp.append('狼人')
    for x in range(Nvwu.number):
        temp.append('女巫')
    for x in range(Yuyanjia.number):
        temp.append('预言家')
    for x in range(Pingmin.number):
        temp.append('平民')
    for x in range(Shouwei.number):
        temp.append('守卫')
    temp=random.choices(temp,k=len(temp))
    for y in range(len(Game)):
        if temp[y]=='狼人':
            Langren.new(Game[y])
            print(Game[y]+'->狼人')
            wx.sendmsg('您的身份是狼人,您将在10s内进入狼人专用群',Game[y])
        elif temp[y]=='女巫':
            Nvwu.new(Game[y])
            print(Game[y]+'->女巫')
            wx.sendmsg('您的身份是女巫',Game[y])
        elif temp[y]=='预言家':
            Yuyanjia.new(Game[y])
            print(Game[y]+'->预言家')
            wx.sendmsg('您的身份是预言家',Game[y])
        elif temp[y]=='守卫':
            Shouwei.new(Game[y])
            print(Game[y]+'->守卫')
            wx.sendmsg('您的身份是守卫',Game[y])
        elif temp[y]=='平民':
            Pingmin.new(Game[y])
            print(Game[y]+'->平民')
            wx.sendmsg('您的身份是平民',Game[y])
        time.sleep(0.5)
    time.sleep(1)
    LangrenGroupup=[]
    wx.send2group('名称分发完毕!')
    for x in range(len(Langrenx)):
        LangrenGroupup.append(x)
    wx.langrengroup(LangrenGroupup)
    mainloop()
def Calculation():
    #结束的统计
    print('游戏结束,暂无统计')
def Gameover():
    #判断
    return False
def Toupiao():
    #遗言 投票
    #自动统计并宣布谁出局
    return
def mainloop():
    global dengdaishouwei
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    wx.send2group('天黑请闭眼!')
    time.sleep(0.5)
    wx.send2group('守卫请睁眼')
    time.sleep(1)
    wx.send2group('守卫请选择对象')
    #选择提示
    #操作完毕等待输入
    dengdaishouwei=True
    while dengdaishouwei:
        time.sleep(1)
    wx.send2group('守卫请闭眼,狼人请睁眼')
    wx.send2langren('请稍后...')
    y=0
    TableStr='请选择对象:'
    for x in Game:
        y=y+1
        if All.alive(x)==Alive:
            Table[y]=x
            TableStr=TableStr+'\n'+str(y)+':'+x
    wx.send2langren(TableStr)
    dengdailangren=True
    while dengdailangren:
        time.sleep(1)
    wx.send2group('狼人请闭眼,女巫请睁眼')
    #选择提示
    #操作完毕等待输入    
    dengdainvwu=True
    while dengdainvwu:
        time.sleep(1)
    wx.send2group('女巫请闭眼,预言家请睁眼')
    #选择提示
    #操作完毕等待输入
    dengdaiyuyanjia=True
    while dengdaiyuyanjia:
        time.sleep(1)
    wx.send2group('天亮了')
    if Gameover()==False:
        Toupiao()
        if Gameover()==False:
            mainloop()
    else:
        #结束统计
        Calculation()
#等待消息(Itchat部分)
@itchat.msg_register(TEXT)
def recv(msg):
    global dengdaishouwei
    global dengdailangren
    global dengdainvwu
    global dengdaiyuyanjia
    global Waiting
    global Game
    if dengdailangren==True:
        if msg['User']['NickName'] in Game:
            if All.job(msg['User']['NickName'])=='狼人' and All.alive(msg['User']['NickName'])==Alive:
                if msg['Content'] in Table:
                    if Langren.kill(Table[msg['Content']]):
                        print('操作成功')
                        wx.send2langren('成功杀死'+Table[msg['Content']])
                    else:
                        print('失败:'+GetError.Error)
            else:
                wx.sendmsg('您无法发送该指令:您不是狼人或您已死',msg['User']['NickName'])
        dengdailangren=False
    if dengdainvwu==True:
        print('### 女巫')
        #判断 女巫是否活着 如果活着就选 挂了就延迟随机
        dengdainvwu=False
    if dengdaishouwei==True:
        print('### 守卫')
        #判断 守卫是否活着 如果活着就选 挂了就延迟随机
        dengdaishouwei=False
    if dengdaiyuyanjia==True:
        print('### 预言家')
        #判断 预言家是否活着 如果活着就选 挂了就延迟随机
        dengdaiyuyanjia=False
    if msg['Content']=='开始游戏':
        #开始游戏
        if msg['User']['NickName'] in Waiting or msg['User']['NickName'] in Game:
            wx.sendmsg('您已在游戏中或在列表中,不能再次开始',msg['User']['NickName'])
        else:
            Wx2Name[msg['FromUserName']]=msg['User']['NickName']
            Name2Wx[msg['User']['NickName']]=msg['FromUserName']
            Waiting.append(msg['User']['NickName'])
            if len(Waiting)==Langren.number+Nvwu.number+Yuyanjia.number+Shouwei.number+Pingmin.number:
                if Game!=[]:
                    wx.sendmsg('无法加入,列表已满,请稍后再试',msg['User']['NickName'])
                    return False
                print('游戏开始')
                wx.group(Waiting)
                Game=Waiting
                Waiting=[]
                startgame()
itchat.run()
