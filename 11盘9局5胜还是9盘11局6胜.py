# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from scipy.special import comb

def calculate_pro(n,p):
    #p为单局胜率，n为比赛总局数,输出总胜率
    assert n%2!=0#n如果是偶数就报错
    m=(n+1)//2
    result=0
    for i in range(m,n+1):#胜利次数
        result+=comb(n,i)*np.power(p,i)*np.power((1-p),n-i)
    return result
def calculate_success(a,b):#a 盘 b局(b+1)/2胜 的胜算
    p_success=[]
    p_range=list(np.linspace(0.5,1,20))#这里可以调整p的取值范围(0.5,1)，以及点数(20)
    for p in p_range:
        p_success.append(calculate_pro(a,calculate_pro(b,p)))
    return plt.plot(p_range,p_success,label='times:%d'%a)#代表盘数
calculate_success(11,9)#11盘9局5胜
calculate_success(9,11)#9盘11局6胜
calculate_success(3,33)#3盘33局17胜
calculate_success(33,3)#33盘3局2胜
calculate_success(99,1)#99盘1局1胜
calculate_success(1,99)#1盘99局50胜
plt.xlabel('p for every match')
plt.ylabel('p')
plt.legend()

