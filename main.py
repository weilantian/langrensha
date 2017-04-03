import sys
import random
import time

from wxpy import *
bot = Bot(cache_path=True)

Player = []
gameStart = False



Wolf = []
Witch = ""
Predictor = ""
Villager = []
Scheduled = []

langrenamout=2
cunminamout=0

@bot.register()
def print_messages(msg):
    global Player
    global gameStart
    if msg.text == "加入游戏" :
        if gameStart == False:
            if msg.sneder in Player:
                return "请不要重复加入"
            else:
                Player.append(msg.sender)
                if len(Player)>=2+langrenamout+cunminamout:
                    role_distribution()
                    # 开始游戏咯～
            
                

def role_distribution():
    global Wolf,Predictor,Villager,Scheduled,chatroomUserClass,langrenChatRoomClass
    Wolf = random.sample(Player)
    for wolf in Wolf :
        wolfMsg = "你的身份是「狼人」，你的同伙为："
        for wwolf in Wolf:
            if wwolf != wolf:
                wolfMsg = wolfMsg + wwolf.remark_name + ""
        wolfMsg = "你们要做的就是保护好自己的身份，然后。。。。你等一下就知道了。。。"
        wolf.send_msg(wolfMsg)
    Scheduled = Wolf
    while Witch != "":
        rdPlayer = random.choice(Player)
        if (rdPlayer not in Scheduled):
            Witch = rdPlayer
            Scheduled.append(Witch)
            Witch.send_msg("你的身份是「女巫」")
    while Predictor != "":
        rdPlayer = random.choice(Player)
        if (rdPlayer not in Scheduled):
            Predictor = rdPlayer
            Scheduled.append(Predictor)
            Predictor.send_msg("你的身份是「预言家」")
    for player in Player:
        if (player not in Scheduled):
            Villager.append(player)
            player.send_msg("您的身份是「平民」")
            Scheduled.append(Villager)
            chatroomUserClass = bot.create_group(player,"狼人杀Beta")
            chatroomUserClass.send_msg("所有的身份已经发放完毕，如有出现没有收到身份等异常翻车情况，请及时私聊。")
            






# 堵塞线程，并进入 Python 命令行
bot.join()