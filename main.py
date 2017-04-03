from wxpy import *

bot = Bot()

Player = []

@bot.register()
def print_messages(msg):
    global Player
    if msg.text == "加入游戏" :
        if len(Player) != 5:
            Player.append(msg.sender)
            return "欢迎加入游戏，您的游戏id为：{}，如需要退出游戏请回复「退出游戏」即可。".format(Player.index(msg.sender))
        else:
            return "当前房间游戏人数已满，请稍后再试。"




# 堵塞线程，并进入 Python 命令行
bot.join()