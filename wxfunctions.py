#wxfunctions
import time
print('wxfunction是基于itchat的一款软件.\nhttps://github.com/littlecodersh/ItChat')
print('本程序需要有活动的网络连接才能工作.')
print('***本程序为插件,不能单独使用,要有recv_callback(msg)函数.***')
Wx2Name={}
Name2Wx={}
groupchatmain=''
groupchatlangren=''
#from langrensha import recv_callback
import itchat
from itchat.content import *
class wx:
    def login(cmdQR=False):
        itchat.auto_login(hotReload=True,enableCmdQR=cmdQR)
    def sendmsg(msg,name):
        itchat.send_msg(msg,toUserName=Name2Wx[name])
    def group(people=None):
        if people==None:
            print('Err')
            return False
        global groupchatmain
        userDict=[]
        for userlist in people:
            userDict.append({"UserName":userlist})
            gctmp=itchat.create_chatroom(userDict, '狼人杀Beta')
            groupchatmain=gctmp['ChatRoomName']
            itchat.send_msg('欢迎加入狼人杀',toUserName=groupchatmain)
            time.sleep(0.1)
            itchat.send_msg('请稍后，正在获取昵称...',toUserName=groupchatmain)
    def langrengroup(people=None):
        global groupchatlangren
        if people==None:
            print('Err')
            return False
        userDict=[]
        for userlist in people:
            userDict.append({"UserName":userlist})
            gctmp=itchat.create_chatroom(userDict, '狼人群-狼人杀Beta')
            groupchatlangren=gctmp['ChatRoomName']
            itchat.send_msg('你们的身份是狼人,这里是给你们讨论的场所\n讨论结束后请其中一个人向服务号发送编号.',toUserName=groupchatmain)
    def send2group(msg):
        itchat.send_msg(msg,toUserName=groupchatmain)
    def send2langren(msg):
        itchat.send_msg(msg,toUserName=groupchatlangren)
