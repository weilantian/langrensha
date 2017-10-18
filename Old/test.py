import sys
import random
import itchat
import time
from itchat.content import *

itchat.auto_login()

itchat.send('狼人杀管理机器人服务以已经启动，请邀请朋友发送「加入狼人杀游戏」进入游戏。')

gameState = 0
player = []

Wolf = []
Witch = ""
Predictor = ""
Villager = []
Scheduled = []
chatroomUserName = ""
langrenChatRoomName = ""

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg['MsgType'] == 1 :
        if msg['Content'] == "加入游戏" :
            if gameState == 0 :
                itchat.send_msg(msg='正在进入游戏...', toUserName=msg['FromUserName'])
                if msg['FromUserName'] not in player :
                    player.append(msg['FromUserName'])
                    if len(player) == 7 :
                        gameState = 1
                        # 游戏召集完毕，创建讨论组，准备开始游戏
                        for Player in player :
                            itchat.send_msg(msg='系统正在抽签安排游戏角色，游戏即将开始，请做好准备',toUserName=Player)
                        Wolf = random.sample(player,3)
                        for wolf in Wolf :
                            msg1 = "你的身份是『狼人』，你的同伙是："
                            for thwolf in Wolf:
                                if wolf != thwolf :
                                    msg1 = msg1 + thwolf + ''
                            itchat.send_msg(msg1,toUserName=wolf)
                        Scheduled = Wolf
                        while Witch != "" :
                            rd = random.choice(player)
                            if (rd not in Wolf) :
                                Witch = rd
                                itchat.send_msg(msg='你的身份是『女巫』',toUserName=Witch)
                                Scheduled.append(Witch)
                        while Predictor != "" :
                            rd = random.choice(player)
                            if (rd not in Scheduled) :
                                Predictor = rd
                                Scheduled.append(Predictor)
                                itchat.send_msg(msg='你的身份是『预言家』',toUserName=Predictor)
                        for Player in player :
                            if (Player not in Scheduled) :
                                Villager.append(Player)
                                itchat.send_msg(msg='你的身份是『村民』',toUserName=Player)
                        chatroomUserName = itchat.create_chatroom(player, '狼人杀Beta')
                        itchat.send_msg(msg='身份牌已经发送完毕，游戏在五秒后正式开始。',toUserName=chatroomUserName)
                        time.sleep(5000)
                        itchat.send_msg(msg='游戏开始，天黑请闭眼。',toUserName=chatroomUserName)
                        time.sleep(1000)
                        langrenChatRoomName = itchat.create_chatroom(player, '狼人杀「狼人」专用讨论组')
                        itchat.send_msg(msg='狼人请睁眼，请狼人们在「狼人专用讨论组中统一意见，并要求其中一位狼人将要杀的人的私聊给裁判。」',toUserName=chatroomUserName)
                        gameState = 2

                        # 将剩余的人全部添加入民
                else :
                    itchat.send_msg(msg='您当前已经进入游戏，回复「退出游戏」可退出游戏', toUserName=msg['FromUserName'])
            else :
                itchat.send_msg(msg='当前游戏已经开始或进入准备状态，请稍后再试。',toUserName=msg['FromUserName'])

itchat.run()
