#lrsclasses.py
Langrenx=[]#狼人列表
Nvwux=[]#女巫列表
Yuyanjiax=[]#预言家列表
Shouweix=[]#守卫列表
Pingminx=[]#平民列表
Protected=''
Alive=True
Dead=False
Players={}
NvwuChance=1
class GetError:
    Error='None'
    IDto=0
class Langren:
    '狼人'
    global Langrenx
    number=0
    def delete(name):
        if name in Langrenx:
            Langrenx.remove(name)
            del(Players[name])
            return True
        else:
            GetError.Error='删除时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
    def new(name):
        if name in Langrenx:
            GetError.Error='创建时出错:名称已存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            Langrenx.append(name)
            Players[name]=True
            return True
    def kill(name):
        Proved=False
        for x in Shouwei:
            if Players[x]==Alive:
                Proved=True
        if Proved==True and name==Protected:
            GetError.Error='守护'
            GetError.IDto=GetError.IDto+1
            return '守护'
        if Players[name]==Alive:
                Players[name]==Dead
                return True
        else:
            GetError.Error='尝试写入时出错:目标玩家已死'
            GetError.IDto=GetError.IDto+1
            return False
class Nvwu:
    '女巫'
    global Nvwux
    number=0
    def delete(name):
        if name in Nvwux:
            Nvwux.remove(name)
            del(Players[name])
            return True
        else:
            GetError.Error='删除时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
    def new(name):
        if name in Nvwux:
            GetError.Error='创建时出错:名称已存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            Nvwux.append(name)
            Players[name]=True
            return True
    def kill(name):
        #什么都没干
        return True
    def save(name):
        if NvwuChance==0:
            GetError.Error='写入时出错:女巫机会已用完'
            GetError.IDto=GetError.IDto+1
            return False
        if name in Players:
            if Players[name]==Dead:
                Players[name]=Alive
                return True
            else:
                GetError.Error='写入时出错:玩家还是活的,不需要救'
                GetError.IDto=GetError.IDto+1
                return False
class Yuyanjia:
    '预言家'
    def delete(name):
        if name in Yuyanjiax:
            Yuyanjiax.remove(name)
            del(Players[name])
            return True
        else:
            GetError.Error='删除时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
    def new(name):
        if name in Yuyanjiax:
            GetError.Error='创建时出错:名称已存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            Yuyanjiax.append(name)
            Players[name]=True
            return True
    def know(name):
        return All.job(name)
class Shouwei:
    def delete(name):
        if name in Shouweix:
            Shouweix.remove(name)
            del(Players[name])
            return True
        else:
            GetError.Error='删除时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
    def new(name):
        if name in Shouweix:
            GetError.Error='创建时出错:名称已存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            Shouweix.append(name)
            Players[name]=True
            return True
    def protect(name):
        if name in Players:
            if name != Protected and Players[name]==Alive:
                Protected=name
                return True
            else:
                GetError.Error='在尝试保护的时候出错:玩家不存在或已在上一轮保护过'
                GetError.IDto=GetError.IDto+1
                return False
class Pingmin:
    '平民,无权限'
    def delete(name):
        if name in Pingminx:
            Pingminx.remove(name)
            del(Players[name])
            return True
        else:
            GetError.Error='删除时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
    def new(name):
        if name in Pingminx:
            GetError.Error='创建时出错:名称已存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            Pingminx.append(name)
            Players[name]=True
            return True
class All:
    '全体玩家控制'
    global Players
    def job(name):
        if name not in Players:
            GetError.Error='获取成员职务时出错:名称不存在'
            GetError.IDto=GetError.IDto+1
            return False
        else:
            if name in Langrenx:
                return '狼人'
            elif name in Yuyanjiax:
                return '预言家'
            elif name in Pingminx:
                return '平民'
            elif name in Nvwux:
                return '女巫'
    def alive(name):
        if name in Players:
            return Players[name]
        else:
            return -1
