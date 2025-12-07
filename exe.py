'''
文件列表:
Event_k.event  事件(by AI)
Execute_k.execution 事件操作(by AI)
history.txt 史书(日志)
'''
try:
    name=input("姓名:")
    gender=int(input("性别(1男|2女)[整数]:"))
    death_age_random_limit=int(input("初始寿命随机上限(推荐135)[整数]"))
    round_times=int(input("轮回次数[整数]"))
except:
    print("输入无效!")
from random import *
from time import sleep
#from tqdm import tqdm
try:
    class human:
        def __init__(self,name,age,gender,IsLiving,death_age,age_max,id,abilities=[]):#变量定义
            self.name=name 
            self.age=age
            self.gender=gender
            self.abilities=abilities
            self.death_age=death_age
            self.isliving=IsLiving
            self.age_max=age_max
            self.id=id
        def spwan(self):#出生
            self.age=0
            if self.gender==1:
                _gender="男孩"
            elif self.gender==2:
                _gender="女孩"
            else:
                _gender="[未知性别 Unknown gender]"
            '''else:
                _gender="沃尔玛购物袋"'''
            print(f"{self.name} 出生了,是个{_gender}.")
        def age_up(self):#生长
            self.age+=1
            #print(f"{self.name}长大了一岁.[{self.age}]")#debug用
        def die(self):#死亡
            if self.age>=self.death_age:
                self.isliving=False
        def random_age_max(self):#寿命最大上限随机函数
            self.age_max=randint(10000,9999999)
            return self.age_max
        def random_id(self):#id生成
            self.id=f"efa{self.age_max}e{randint(1,99)}a32f{self.death_age}" 
            return self.id         
        def GetEventFiles(self):#获取事件文件
            f=open("Event_k.event","r")
            _s=f.read()
            e=_s.split("\n")
            f.close()
            return e
        def GetExecutionEventOfFiles(self):#获取事件操作文件
            f1=open("Execute_k.execution","r")
            _s=f1.read()
            ex=_s.split("\n")
            f1.close()
            return ex
        def ExecuteEventsOfFiles(self,l_e=[100],l_x=[100]):#输出事件执行操作
            rn=randint(0,len(l_e))
            event=l_e[rn-1]
            print(f"{self.name}({self.age}/{self.death_age}[{self.age_max}]) {event}({l_x[rn-1]})")#I
            exec(l_x[rn-1])
            return event
        def reset(self):#重置
            self.isliving=True
            self.age=0
            self.death_age=randint(0,150)
            self.abilities=[]
            self.random_age_max()
            self.random_id()
except FileNotFoundError():
    print("文件缺失(事件文件\"Event_k.event\"或事件操作文件\"Execute_k.execution\")!")
except:
    print("未预料的错误!")
'''-----------------------------------------------------------------------------'''
try:
    n=human(name=name,gender=gender,death_age=randint(0,death_age_random_limit),age=int,IsLiving=True,age_max=None,id=None)#name->姓名,gender->性别
    e_k=n.GetEventFiles()
    exe_k=n.GetExecutionEventOfFiles()
    n.spwan()
    n.random_age_max()
    n.random_id()
    #print(e_k,exe_k)#debug用
    f_h=open("history.txt","a")
    f_h.write(f"\nid:{n.id}\n[Record Began]\n")
    print(f"{n.id}\n[Record Began]\n")
    for i in range(round_times):#轮回次数
        round_text=f"第{i+1}世轮回\n"#轮回开始描述文本
        f_h.write(f"{round_text}")
        print(f"{round_text}")
        while n.isliving!=False: 
            n.age_up()
            f_h.write(f"{n.name}({n.age}/{n.death_age}[{n.age_max}]){n.ExecuteEventsOfFiles(e_k,exe_k)}\n")#姓名(当前岁数/寿命[寿命最高上限])发生的重大事件
            n.die()
            if n.age >=n.age_max:
                break
            #sleep(0.51)#debug用
        end_text=f"{n.name}与世长辞,享年{n.age}(/{n.death_age}[{n.age_max}])岁.\n{n.name}再次踏上了轮回...\n[Record End]\n@[System]:\n命中注定:{n.death_age}(最高上限:{n.age_max})\n现实终点:{n.age}\n能力:{n.abilities}\n#由{n.id}参演#\n*System shutdown*\n\n"
        #(上方)结语文字
        print(f"{end_text}")#输出结语
        f_h.write(f"{end_text}")#记录结语
        n.reset()#踏上下一轮回(重置)
except:
    print("未预料的错误!")
finally:
    f_h.close()