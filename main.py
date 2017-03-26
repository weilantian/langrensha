import sys
import itchat
from itchat.content import *

itchat.auto_login()

itchat.send('狼人杀管理机器人服务以已经启动，请邀请朋友发送「加入狼人杀游戏」进入游戏。')

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg['MsgType'] == 1 :
        print('收到一条文本消息')

itchat.run()