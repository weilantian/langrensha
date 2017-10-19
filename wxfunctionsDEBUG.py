#wxfunctionsDEBUG
import time
print('wxfunctionDEBUG - 仅供测试使用')
Wx2Name={}
Name2Wx={}
groupchatmain=''
groupchatlangren=''
#from langrensha import recv_callback
#import itchat
#from itchat.content import *
class wx:
    def login(cmdQR=False):
        #itchat.auto_login(hotReload=True,enableCmdQR=cmdQR)
        print('自动登陆')
    def sendmsg(msg,name):
        print('向'+name+'发送消息:'+msg)
        print('微信id为:'+Name2Wx[name])
        #itchat.send_msg(msg,toUserName=Name2Wx[name])
    def group(people=None):
        if people==None:
            print('Err')
            return False
        global groupchatmain
        userDict=[]
        for userlist in people:
            userDict.append({"UserName":userlist})
        print('创建主群，成员为:')
        print(userDict)
        #gctmp=itchat.create_chatroom(userDict, '狼人杀Beta')
        #groupchatmain=gctmp['ChatRoomName']
        #itchat.send_msg('欢迎加入狼人杀',toUserName=groupchatmain)
        print('向主群发送消息:欢迎加入狼人杀')
        time.sleep(0.1)
        #itchat.send_msg('请稍后，正在获取昵称...',toUserName=groupchatmain)
    def langrengroup(people=None):
        global groupchatlangren
        if people==None:
            print('Err')
            return False
        userDict=[]
        for userlist in people:
            userDict.append({"UserName":userlist})
            print('创建群组:狼人群-狼人杀Beta 成员列表:')
            print(userDict)
            #gctmp=itchat.create_chatroom(userDict, '狼人群-狼人杀Beta')
            #groupchatlangren=gctmp['ChatRoomName']
            #itchat.send_msg('你们的身份是狼人,这里是给你们讨论的场所\n讨论结束后请其中一个人向服务号发送编号.',toUserName=groupchatmain)
            print('向狼人群发送:你们的身份是狼人,这里是给你们讨论的场所\n讨论结束后请其中一个人向服务号发送编号.')
    def send2group(msg):
        print('向主群发送:'+msg)
        #itchat.send_msg(msg,toUserName=groupchatmain)
    def send2langren(msg):
        print('向狼人群发送:'+msg)
        #itchat.send_msg(msg,toUserName=groupchatlangren)
