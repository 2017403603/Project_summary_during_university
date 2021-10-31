# coding=utf-8
import math
import numpy as np
'''
测试函数
'''
def GrieFunc(vardim, x, bound):
    """
    Griewangk function
    函数解释随着量变而改变，函数的真个数据分布中存在大量局部极值.。检测算法跳出局部的能力
    全局最小值 f(0) = 0
    """
    s1 = 0.
    s2 = 1.
    for i in range(1, vardim + 1):
        s1 = s1 + x[i - 1] ** 2
        s2 = s2 * math.cos(x[i - 1] / math.sqrt(i))
    y = (1. / 4000.) * s1 - s2 + 1
    #y = 1. / (1. + y)
    return y


def Rastrigin(vardim, x, bound):
    """
    Rastrigin function
    此函数是基于De Jong函数，增加了一个余弦调制传递函数来产生频繁的局部最小值
    特点： 极小值的位置是有规律的
    用来检测在解有规律的一种情况，算法的实用性
    """
    s = 0
    for i in range(vardim):
        s = s + ((x[i]) ** 2 - 10 * math.cos(2 * math.pi * (x[i]))+10)
    return s

def Ackley(vardim,x,bound):
    X = np.array(x)
    X = X
    sum_x = np.sum(X ** 2)
    sum_cos_x = 0
    for i in range(len(x)):
        sum_cos_x += np.cos(2 * np.pi * X[i])

    part_1 = -20.0 * np.exp(-0.2 * np.sqrt(sum_x / vardim))
    part_2 = -np.exp(sum_cos_x / vardim)
    t1 = part_1  + 20.0
    t2 = np.exp(1.0)+ part_2
    result =  t1 + t2
    return  result


def Sphere(vardim,x,bound):
    s = 0
    for i in range(vardim):
        s = s + x[i]**2

    return s

def Rosenbrock(vardim,x,bound):
    s = 0
    for i in range(vardim-1):
        a = (x[i+1]-x[i]**2)**2
        b = (x[i] - 1)**2
        s = s + 100*a + b

    return s

def Weierstrass(vardim,x,bound):
    s=0
    a=0.5
    b=0.3
    kmax=20
    c=d=0
    for k in range(0,kmax):
        d+=pow(a,k)*math.cos(2*math.pi*pow(b,k)*0.5)
    d*=vardim
    for i in range(vardim):
        temp=0
        for k in range(0, kmax):
            temp+=pow(a,k)*math.cos(2*math.pi*pow(b,k)*(x[i]+0.5))
        c+=temp
    s=c-d+1
    return s
def Noncontinuous_Rastrigin(vardim,x,bound):
    y=np.zeros(vardim)
    for i in range(0,vardim):
        if x[i]<0.5:
            y[i]=x[i]
        else:
            y[i]=round(2*x[i])/2.0
    return Rastrigin(vardim,y,bound)
def Schwefel(vardim,x,bound):
    a=418.9829*vardim
    b=0
    for i in range(0, vardim):
        b+=x[i]*math.sin(math.sqrt(abs(x[i])))
    s=a-b
    return s
def Levy(vardim,x,bound):
    a=0
    for i in range(0,vardim-1):
        a+=(x[i]-1)**2*(1+pow(math.sin(3*math.pi*x[i+1]),2))
    s=a+pow(math.sin(3*math.pi*x[0]),2)+abs(x[vardim-1]-1)*(1+pow(math.sin(3*math.pi*x[vardim-1]),2))
    return s
def Bohachevsky(vardim,x,bound):
    s=0
    for i in range(0, vardim - 1):
        s+=x[i]**2+2*(x[i+1]**2)-0.3*math.cos(3*math.pi*x[i])-0.4*math.cos(4*math.pi*x[i+1])+0.7
    return s
def Alpine1(vardim,x,bound):
    s=0
    for i in range(0, vardim ):
        s+=abs(x[i]*math.sin(x[i])+0.1*x[i])
    return s
def Shubert(vardim,x,bound):
    s=1
    for i in range(0, vardim):
        temp=0
        for j in range(1,6):
            temp+=j*math.cos((j+1)*x[i]+j)
        s*=temp
    return s
def Trid10(vardim,x,bound):
    s = 0
    b=a=0
    for i in range(0, vardim):
        a+=(x[i]-1)**2
    for i in range(1, vardim):
        b+=x[i]*x[i-1]
    s=a-b
    return s