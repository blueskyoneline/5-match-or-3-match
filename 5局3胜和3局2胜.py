# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
from scipy.special import comb

def calculate_pro(n,p):
    #p为单局胜率，n为比赛总局数
    assert n%2!=0#n如果是偶数就报错
    m=(n+1)//2
    result=0
    for i in range(m,n+1):#胜利次数
        result+=comb(n,i)*np.power(p,i)*np.power((1-p),n-i)
    return result
def calculate_success(n):#比赛总局数
    p_success=[]
    p_range=list(np.linspace(0.5,1,6))#这里可以调整p的取值范围(0.5,1)，以及点数(6)
    for p in p_range:
        p_success.append(calculate_pro(n,p))
    return plt.plot(p_range,p_success,label='times:%d'%n)
calculate_success(3)#3局2胜
calculate_success(5)#5局3胜
calculate_success(7)#7局4胜
calculate_success(9)#9局5胜
calculate_success(11)#11局6胜
plt.xlabel('p for every match')
plt.ylabel('p')
plt.legend()

