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
IsAlive = []
WillKilled = []
Tacket = []
chatroomUserClass = ""
totalNum = 7

nowGameStatus = 0

@bot.register()
def print_messages(msg):
    global Player
    global gameStart
    global WillKilled
    if msg.text == "加入游戏" :
        if not gameStart:
            if msg.sneder in Player:
                return "请不要重复加入"
            else:
                Player.append(msg.sender)
                msg.sender.send_msg("欢迎加入游戏，您再游戏中的id为",str(Player.index(msg.sender)),"，加入游戏后不得退出游戏。")
                if len(Player) >= totalNum:
                    role_distribution()
                    # 开始游戏咯～

    elif msg.text[:5] == "我们决定要杀":
        if nowGameStatus == 1:
            if msg.sender in Wolf and IsAlive[Player.index(msg.sender)]:
                if len(chatroomUserClass.search(msg.text)) != 0:
                    WillKilled.append(chatroomUserClass.search(msg.text[6:])[0])
                    nowGameStatus = 2
                    return "好的我知道了"
                else:
                    return "并没有这个人"
            else:
                return "你当前的身份不是狼人或者你已经死了，不能发言"
        else:
            return "当前不是狼人的发言时间。"

    elif msg.text[:1] == "救":
        if nowGameStatus == 2:
            if msg.sender == Witch and IsAlive[Player.index(msg.sender)]:
                if len(chatroomUserClass.search(msg.text)) != 0:
                    if (chatroomUserClass.search(msg.text[1:])[0] in WillKilled):
                        WillKilled.remove(chatroomUserClass.search(msg.text[1:])[0])
                    nowGameStatus = 3
                    return "好的我知道了"
                else :
                    return "游戏中没有这个人"
            else :
                return "您当前的游戏身份不是女巫或你处于死亡观战状态"
        else :
            return "现在不是女巫发言。"

    elif msg.text[:1] == "毒":
        if nowGameStatus == 2:
            if msg.sender == Witch and IsAlive[Player.index(msg.sender)]:
                if len(chatRoomUserClass.search(msg.text)) != 0:
                    if (chatroomUserClass.search(msg.text[1:])[0] not in WillKilled):
                        WillKilled.append(chatroomUserClass.search(msg.text[2:])[0])
                    nowGameStatus = 3
                    return "好的我知道了"
                else :
                    return "游戏中没有这个人"
            else :
                return "您当前的游戏身份不是女巫或你处于死亡观战状态"
        else :
            return "现在不是女巫发言。"

    elif msg.text[:3] == "我想知道":
        if nowGameStatus == 3:
            if msg.sender == Predictor and IsAlive[Player.index(msg.sender)]:
                if len(chatroomUserClass.serach(msg.text[4:])) != 0:
                    if (chatroomUserClass.serach(msg.text[4:])[0] in Wolf):
                        return "没错，她（他）是狼人"
                    elif (chatroomUserClass.serach(msg.text[4:])[0] == Witch):
                        return "她（他）是女巫"
                    elif (chatroomUserClass,serach(msg.text[4:])[0] == Predictor):
                        return "她（他）是你自己 = ="
                    elif (chatroomUserClass.serach(msg.text[4:])[0] in Villager):
                        return "她（他）是村民"
                    nowGameStatus = 4
                else:
                    return "对不起，没有这个人"
            else:
                return "您不是预言家活着已经死亡"
        else:
            return "当前不是预言家的提问环节。"

@bot.register(Group, TEXT)
def qunneifayan(msg):
    if msg.sender in WillKilled:
        msg.reply("好的，谢谢你的观点。")
        WillKilled.remove(msg.sender)
        IsAlive[Player.index(msg.sender)] = False
    elif nowGameStatus == 4:
        print("do something.....")


                    



    

        

            
                

def role_distribution():
    global Wolf,Predictor,Villager,Scheduled,chatroomUserClass,langrenChatRoomClass,IsAlive
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
            chatroomUserClass.send_msg("所有的身份已经发放完毕，如有出现没有收到身份等异常翻车情况，请及时私聊，如没毛病，5秒钟后将进入游戏")
            time.sleep(5000)
            
            for i in range(0,len(Player)-1):
                IsAlive[i] = True
                #游戏开始前初始化每个人的死亡状态为「活着」
            main_loop()

def main_loop():

    chatroomUserClass.send_msg("新的一个晚上。天黑请闭眼。")
    # 游戏大循环
    if gameStart == True:
        nowGameStatus = 1
        chatroomUserClass.send_msg("先请狼人出没，在狼人专用聊天群中交流要杀的人，并请其中一人将要杀的以「我们决定要杀+昵称的格式私聊给我。")
        while nowGameStatus == 1:
            wait = True
            # 卡在这里直到狼人完成发言
        if (IsAlive[Player.index(Witch)]):
            chatroomUserClass.send_msg("好的，狼人已经完成了杀人，接着，请女巫睁眼，请问你是要毒人（对我私聊毒+昵称）还是要救人（对我私聊救+昵称）？")
            while nowGameStatus == 2:
                wait = True
            # 日常等待发言
        if (IsAlive[Player.index(Villager)]):
            chatroomUserClass.send_msg("好的，那么女巫完成了本轮发言，接着，请预言家睁眼，请问你想知道谁的身份？（对我私聊我想知道+昵称）")
            while nowGameStatus == 3:
                wait = True

        chatroomUserClass.send_msg("天亮了，昨晚")
        for willkilled in WillKilled:
            chatroomUserClass.send_msg(willkilled.remark_name)
        chatroomUserClass.send_msg("被杀，请留遗言。")
        
        for willkilled in WillKilled:
            chatroomUserClass.sned_msg("下面，请"+willkilled.remark_name+"做出表态。")
            while willkilled in WillKilled:
                wait = True
                # 直到发言之后。。。

        chatroomUserClass.send_msg("下面，是最激动人心的投票观点，请给位发送投票+昵称的方式投票。")
        nowGameStatus = 4
        

        
        
        
    '''
    游戏大循环
    '''
    print("GAME START")
            






# 堵塞线程，并进入 Python 命令行
bot.join()