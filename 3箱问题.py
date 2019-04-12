# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:19:49 2019

@author: blueskyoneline
"""
# -*- coding: utf-8 -*-
import random
box=['A','B','C'] #三个箱子命名为A,B,C
plan='change' #换还是不换,可以改为 "unchange"
def host_know():
    t=0#记录中奖个数
    f=0#记录没中奖个数
    n=0#记录总实验次数
    for i in range(10000): #进行10000次试验
        ball=random.choice(box) #ball代表奖品，随机一个箱子
        guest_choice=random.choice(box)#嘉宾随机选择一个箱子
        if guest_choice==ball:
            host_choice=random.choice(list(set(box)-{ball}))
            #如果嘉宾选的对，主持人从其余箱子中随便选一个
        else:
            host_choice=random.choice(list(set(box)-{ball,guest_choice}))
            #如果嘉宾选的不对，主持人选择除嘉宾和奖品外的最后一个箱子
        if plan=='change':
            guest_choice=list(set(box)-{host_choice,guest_choice})[0]
            #如果选择换，就换成除主持和自己选择外的最后一个
        if guest_choice==ball: #如果选中
            t=t+1 #中奖个数+1
        else: #如果不中
            f=f+1 #不中奖个数+1
        n=n+1 #无论结果如何，试验次数+1
    print("主持人知情，中奖频率为：",t/n)

def host_unknow():
    t=0#记录中奖个数
    f=0#记录没中奖个数
    n=0#记录总实验次数
    for i in range(10000): #进行10000次试验
        ball=random.choice(box) #ball代表奖品，随机一个箱子
        guest_choice=random.choice(box)#嘉宾随机选择一个箱子
        host_choice=random.choice(list(set(box)-{guest_choice}))#主持人随机选择一个嘉宾没选的箱子
        if host_choice==ball:
            #主持人选中奖品箱子，这期节目不播了！开始下一轮试验
            continue
        if plan=='change':
            guest_choice=list(set(box)-{host_choice,guest_choice})[0]
            #如果选择换，就换成除主持和自己选择外的最后一个
        if ball==guest_choice:
            t=t+1
        else:
            f=f+1
        n=n+1
    print("主持人不知情，中奖频率为：",t/n)
                
                
host_know()
host_unknow()
                
                
                
                
                
                
                
                
                
                
                
                