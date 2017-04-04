# -*- coding:utf-8 -*-
#Producer:Xiaolan,Yyj
#Github Link:https://github.com/weilantian/langrensha
#变量注释：
#userlist：格式 ['微信id','微信id',...]
#role: 格式 {游戏id:'langren/nvwu/yuyanjia/cunmin',游戏id:'...'}
#idnow： 游戏进入分配id使用
#weuser： 格式{'微信id':'游戏id',...}
#user: 格式{'游戏id':'微信id',...}
#rolelist： 和userlist相同，临时dict，分配角色使用，使用完毕后通过遍历然后用pop删除
import os
import itchat
from itchat.content import *
import sys
import time
import random
idnow=0
ifgame=False
user={}
weuser={}
role={}
userlist=[]
dead=[]
wait=''
save=''
ifchosen=False
groupchatmain=''
groupchatlangren=''
langren=[]
z=''
nvwuwait=''
wefriendnc={}
toupiao=[]
cunmin=[]
nvwu=''
x=0
die=''
yuyanjia=''
roles=['langren','nvwu','yuyanjia','cunmin']
langrenamout=3
cunminamout=3
friendnc={}
itchat.auto_login(hotReload=True)
@itchat.msg_register([TEXT])
def text_reply(msg):
    global idnow
    global user
    global weuser
    global role
    global x
    global userlist
    global nvwuwait
    global wait
    global dead
    global ifchosen
    global save
    global ifgame
    global die
    global toupiao
    if msg['Content']=='开始游戏':
        if ifgame==False:

            if not weuser.get(msg['FromUserName'],-1)==-1:
                itchat.send_msg('请勿重复加入。',toUserName=msg['FromUserName'])
            else:
                itchat.send_msg('加入成功，您的id:%s\n请等待游戏开始.\n游戏开始前，您也可以输入\"退出游戏\"来退出游戏。'%idnow,toUserName=msg['FromUserName'])
                user[idnow]=msg['FromUserName']
                weuser[msg['FromUserName']]=idnow
                userlist.append(msg['FromUserName'])
                print(user)
                print(weuser)
                idnow=idnow+1
                if len(userlist)>=2+langrenamout+cunminamout:
                    #开始游戏
                    start()
        else:
            itchat.send_msg("游戏已开始，请稍后再试",toUserName=msg['FromUserName'])
    if msg['Content']=='退出游戏':
        k=weuser.get(msg['FromUserName'],-1)
        if k!=-1:
            for (a,b) in user.items():
                if b==msg['FromUserName']:
                    fa=a
            for (c,d) in weuser.items():
                if c==msg['FromUserName']:
                    fc=c
            user.pop(fa)
            weuser.pop(fc)
            for us in range(len(userlist)):
                if userlist[us]==msg['FromUserName']:
                    fus=us
            userlist.pop(us)
            itchat.send_msg('成功退出游戏。',toUserName=msg['FromUserName'])
        else:
            itchat.send_msg('退出失败，您未加入游戏.',toUserName=msg['FromUserName'])
        print(userlist)
        print(weuser)
        print(role)
        print(user)
    if msg['FromUserName'] not in userlist:
            print('请先加入游戏。回复\"开始游戏\"')
            itchat.send_msg('请先加入游戏。回复\"开始游戏\"\n--狼人杀Beta',msg['FromUserName'])
            return
    #if各种控制模块
    print(role)
    if ifchosen==False:
        return
    if wait=='toupiao':
        if msg['FromUserName'] not in dead:
            itchat.send_msg('投票成功。',toUserName=msg['FromUserName'])
            toupiao.append(msg['Content'])
    if role[weuser[msg['FromUserName']]]=='langren':
        print('langren says:%s'%msg['Content'])
        print (weuser)
        print (user)
        print(msg['Content'])
        if int(msg['Content']) in user==False:
            itchat.send_msg('对方不存在。',toUserName=msg['FromUserName'])
        elif int(msg['Content']) in dead:
            itchat.send_msg('对方已死，请重新选择',toUserName=msg['FromUserName'])
        elif wait!='langren':
            itchat.send_msg('您现在不能杀人。',toUserName=msg['FromUserName'])
        else:
            dead.append(msg['Content'])
            die=msg['Content']
            wait=''
            goon()
        #狼人发来的消息
    elif role[weuser[msg['FromUserName']]]=='nvwu':
        print('nvwu says:%s'%msg['Content'])
        if wait=='nvwu':
            if nvwuwait!='':
                if msg['Content']=='救':
                    for k in range(len(dead)):
                        if dead[k]==msg['Content']:
                            dead.pop(k)
                            break
                    itchat.send_msg('操作成功',toUserName=msg['FromUserName'])
                    if msg['Content']==die:
                        die=''
                    nvwuwait=''
                    wait=''
                elif msg['Content']=='不救':
                    itchat.send_msg('操作成功',toUserName=msg['FromUserName'])
                    nvwuwait=''
                    wait=''
                    save=msg['Content']
                nvwugoon()
            if int(msg['Content']) in user==False:
                itchat.send_msg('对方不存在。',toUserName=msg['FromUserName'])
            elif wait!='nvwu':
                itchat.send_msg('您现在不能杀人或救人。',toUserName=msg['FromUserName'])
            elif int(msg['Content']) in dead:
                itchat.send_msg('对方已死，请选择救/不救',toUserName=msg['FromUserName'])
                nvwuwait=msg['Content']
        #女巫发来的消息，作消息处理
    elif role[weuser[msg['FromUserName']]]=='yuyanjia':
        print('Yuyanjia says:%s'%msg['Content'])
        if wait=='yuyanjia':
            if int(msg['Content']) in user ==False:
                itchat.send_msg('id不存在，请重新输入',toUserName=msg['FromUserName'])
                return
            itchat.send_msg('%s'%role[msg['Content']])
            wait=''
            yuyanjiagoon()
        #预言家发来的消息，作消息处理
    else:
        print('Cunmin says:%s'%msg['Content'])
        #村民发来的消息
def start():
    global idnow
    global user
    global weuser
    global role
    global roles
    global wefriendnc
    global userlist
    global groupchatlangren
    global groupchatmain
    global ifgame
    global langrenamout
    global cunminamout
    global yuyanjia
    global cunmin
    global langren
    global nvwu
    global x
    global ifchosen
    global friendnc
    ifgame=True
    #初始化
    #包含分配角色 建群等
    #建群获得的id赋值给groupchatmain和groupchatlangren
    print('Out=Userlist')
    print(userlist)
    userDict = []
    for uuserlist in userlist :
        userDict.append({"UserName":uuserlist})
    gctmp=itchat.create_chatroom(userDict, '狼人杀Beta')
    groupchatmain=gctmp['ChatRoomName']
    itchat.send_msg('欢迎加入狼人杀',toUserName=groupchatmain)
    itchat.send_msg('请稍后，正在获取昵称...',toUserName=groupchatmain)
    for x in userlist:
        y=itchat.search_friends(userName=x)
        friendnc[weuser[x]]=y['NickName']
        wefriendnc[y['NickName']]=weuser[x]
    itchat.send_msg('系统将抽取每个人的身份，请留意私信！',toUserName=groupchatmain)
    userDict=[]
    for rolex in userlist:
        rolext=random.choice(roles)
        if rolext=='langren':
            if len(langren)>=langrenamout:
                for x in range(len(roles)):
                    if roles[x]=='langren':
                        roles.pop(x)
                        break
                rolext=random.choice(roles)
                print('******')
                print(roles)
        if rolext=='cunmin':
            if len(cunmin)>=cunminamout:
                for x in range(len(roles)):
                    if roles[x]=='cunmin':
                        roles.pop(x)
                        break
                rolext=random.choice(roles)              
        if rolext=='nvwu':
            if nvwu!='':
                for x in range(len(roles)):
                    if roles[x]=='nvwu':
                        roles.pop(x)
                        break
                rolext=random.choice(roles)
        if rolext=='yuyanjia':
            if yuyanjia!='':
                for x in range(len(roles)):
                    if roles[x]=='yuyanjia':
                        roles.pop(x)
                        break
                rolext=random.choice(roles)
        role[weuser[rolex]]=rolext
        print(weuser[rolex])
        print(roles)
        print(role)
        print(rolex)
        print(rolext)
        if rolext=='langren':
            langren.append(weuser[rolex])
            itchat.send_msg('您的身份是狼人，稍后将进入狼人专用群。',toUserName=rolex)
        if rolext=='cunmin':
            cunmin.append(weuser[rolex])
            itchat.send_msg('您的身份是村民',toUserName=rolex)
        if rolext=='nvwu':
            nvwu=weuser[rolex]
            itchat.send_msg('您的身份是女巫，您有以下技能\n在提示时输入用户id，然后输入救/杀，如：',toUserName=rolex)
            itchat.send_msg('1',toUserName=rolex)
            itchat.send_msg('救',toUserName=rolex)
        if rolext=='yuyanjia':
            yuyanjia=weuser[rolex]
            itchat.send_msg('您的身份是预言家，您有以下技能\n在提示时输入用户id，查看用户身份',toUserName=rolex)
    ifchosen=True
    itchat.send_msg('身份发送完毕，现在开始游戏。',toUserName=groupchatmain)
    for ux in langren:
        userDict.append({"UserName":user[ux]})
    gctmp=itchat.create_chatroom(userDict, '狼人群-狼人杀Beta')
    groupchatlangren=gctmp['ChatRoomName']
    print(gctmp)
    print('狼人群 id%s'%groupchatlangren)
    itchat.send_msg('欢迎来到狼人群。',toUserName=groupchatlangren)
    mainloop()
@itchat.msg_register([TEXT],isGroupChat=True)
def wechat(msg):
    print(msg['Content'])
def mainloop():
    global user
    global wefriendnc
    global weuser
    global role
    global wait
    global z
    global userlist
    #大循环[天黑请闭眼--天亮请睁眼--下一次天黑请闭眼]
    #各种判断模块，判断谁被杀以及剧情发展
    #最后如果女巫/预言家被杀，仍然要一个random的sleep
    #如果所有非狼人/狼人被杀完，游戏结束进入ending，开始120秒倒计时然后强制踢出所有人
    print(wefriendnc)
    for x in friendnc:
        print(x)
        itchat.send_msg(str(x)+"是"+friendnc[x],toUserName=groupchatmain)
        itchat.send_msg(str(x)+'是'+friendnc[x],toUserName=groupchatlangren)
    itchat.send_msg('天黑请闭眼，狼人请睁眼',toUserName=groupchatmain)
    itchat.send_msg('请讨论，选出想杀的人，派一个代表私聊回复id号',toUserName=groupchatlangren)
    wait='langren'
def ending(winner):
    global user
    global weuser
    global role
    global userlist
    global groupchatlangren
    global groupchatmain
    itchat.send_msg('游戏结束。获胜者：%s\n请自行删除并退出。'%winner,toUserName=groupchatmain)
    itchat.send_msg('游戏结束。获胜者：%s\n请自行删除并退出。'%winner,toUserName=groupchatlangren)
    userDict = []
    #初始化
    global idnow
    global roles
    global ifgame
    global langrenamout
    global cunminamout
    global yuyanjia
    global cunmin
    global langren
    global nvwu
    idnow=0
    ifgame=False
    user={}
    weuser={}
    role={}
    userlist=[]
    ifchosen=False
    groupchatmain=''
    groupchatlangren=''
    langren=[]
    cunmin=[]
    nvwu=''
    yuyanjia=''
    roles=['langren','nvwu','yuyanjia','cunmin']
    #各种结果公布+倒计时踢人
def goon():
    itchat.send_msg('狼人发言完毕，请狼人闭眼，请女巫睁眼',toUserName=groupchatmain)
    wait='nvwu'
    itchat.send_msg('昨天晚上%s被杀，请输入id号，然后输入救/不救',toUserName=user[nvwu])
def nvwugoon():
    itchat.send_msg('女巫发言完毕，请女巫闭眼',toUserName=groupchatmain)
    itchat.send_msg('请预言家睁眼',toUserName=groupchatmain)
    wait='yuyanjia'
    itchat.send_msg('请输入您想查询的id号',toUserName=user[yuyanjia])
def yuyanjiagoon():
    wait=''
    itchat.send_msg('预言家发言完毕，天亮了，请睁眼。',toUserName=groupchatmain)
    if save=='':
        save='没有人'
    if die=='':
        die='没有人'
    itchat.send_msg('昨天%s被杀死，%s被救'%die,save)
    if save!='没有人':
        itchat.send_msg('您有60秒的时间讨论并私聊投票，已死者不能参与。',toUserName=groupchatmain)
        wait='toupiao'
        time.sleep(60)
        wait=''
        x=get_mode(toupiao)
        if x==None:
            itchat.send_msg('没有相同的投票，投票无效，进入下一轮',toUserName=groupchatmain)
        elif len(x)>1:
            y=random.choice(x)
            dead.append(y)
            itchat.send_msg('%s被杀死'%y,toUserName=groupchatmain)
        elif len(x)==1:
            itchat.send_msg('%s被杀死'%x[0],toUserName=groupchatmain)
            dead.append(x[0])
        mainloop()
def get_mode(arr):  
    mode = [];  
    arr_appear = dict((a, arr.count(a)) for a in arr);  # 统计各个元素出现的次数  
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1  
        return;  # 则没有众数  
    else:  
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(arr_appear.values()):  
                mode.append(k);  
    return mode;
itchat.run()
