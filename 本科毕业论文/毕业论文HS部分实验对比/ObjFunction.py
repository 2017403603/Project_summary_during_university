import math
import numpy as np
import random
'''
测试函数
'''
def Griewank(vardim, x, bound):
    s1 = 0.
    s2 = 1.
    for i in range(1, vardim + 1):
        s1 = s1 + (x[i - 1])** 2
        s2 = s2 * math.cos((x[i - 1])/ math.sqrt(i))
    y = (1. / 4000.) * s1 - s2 + 1

    return y


def Rastrigin_move(vardim, x, bound):
    s = 0
    for i in range(vardim):
        x1 = x[i]-1
        s = s + (x1)**2 - 10*math.cos(2*math.pi*x1)+10
    return s


def Rastrigin(vardim, x, bound):
    s = 0.0
    pi=math.pi
    for i in range(vardim):
        s = s + (x[i]*x[i] - 10 * math.cos(2 * pi * x[i])+10)
    return s

def Ackley_shift(vardim,x,bound):
    X = np.array(x)
    X = X - 1
    sum_x = np.sum(X ** 2)
    sum_cos_x = 0
    for i in range(len(x)):
        sum_cos_x += np.cos(2 * np.pi * X[i])
    len_x = len(x)
    part_1 = -20 * np.exp(-0.2 * np.sqrt(sum_x / len_x))
    part_2 = -np.exp(sum_cos_x / len_x)
    result = part_1  + 20 + np.e + part_2
    return result


def Ackley(vardim,x,bound):
    X = np.array(x)
    X = X
    sum_x = np.sum(X ** 2)
    sum_cos_x = 0
    for i in range(len(x)):
        sum_cos_x += np.cos(2 * np.pi * X[i])
    part_1 = -20.0 * np.exp(-0.2 * np.sqrt(sum_x / vardim))
    part_2 = -np.exp(sum_cos_x / vardim)
    t1 = part_1 + 20.0
    t2 = np.exp(1.0) + part_2
    result = t1 + t2
    return result


def Sphere(vardim,x,bound):
    s = 0
    for i in range(vardim):
        s = s + (x[i])**2

    return s


def Step(vardim,x,bound): #！！！
    # s = 0
    # for i in range(vardim):
    #     z = (x[i]+0.5)**2
    #     s = s+z
    #
    # return s
    X = np.array(x)
    x1 = X + 0.5
    x2 = np.square(x1)
    resutlt = np.sum(x2)
    return resutlt


def Schwefel221(vardim,x,bound):
    max = math.fabs(x[0])
    for i in range(vardim):
        z = math.fabs(x[i])
        if max<z:
            max = z

    return max


def Schwefel222(vardim,x,bound):
    sum1 = 0
    c = 1
    for i in range(vardim):
        sum1 = sum1+math.fabs(x[i])
        c = c*math.fabs(x[i])

    return sum1 + c


def six_Hump_camel_back(vardim,x,bound):
    y = 4*(x[0]**2) - 2.1*(x[0]**4) + (x[0]**6)/3 + (x[0]*x[1]) -4*(x[1]**2) + 4*(x[1]**4)
    return y

def Alpine1(vardim,x,bound):
    y = 0
    for i in range(vardim):
        z = x[i]*math.sin(x[i]) + 0.1*x[i]
        y = y + math.fabs(z)

    return y


def Trid(vardim, x, bound):
    y1 = 0
    y2 = 0
    # for i in range(vardim):

    for i in range(vardim-1):
        x1 = (x[i]-1)**2
        y1 = y1 + x1
        x2 = x[i]*x[i+1]
        y2 = y2 + x2
    y1 = y1 + x[i+1]**2
    return y1-y2


def Drop_Wave(vardim, x, bound):
    x1 = 1 + math.cos(12*math.sqrt(x[1]**2+x[0]**2))
    x2 = (x[1]**2+x[0]**2)*0.5 + 2
    return -1*(x1/x2)


def Eggholder(vardim, x, bound):
    x1 = (x[1]+47)*math.sin(math.sqrt(math.fabs(x[1]+x[0]/2+47)))
    x2 = (x[0]*math.sin(math.sqrt(math.fabs(x[0]-x[1]-47))))

    return -x1-x2


def Quartic(vardim, x, bound):
    y = 0
    for i in range(vardim):
        z = (i+1)*math.pow(x[i],4)
        y = y+z

    return  y + np.random.uniform(0,1)



def Shubert(vardim,x,bound):
    s=1
    for i in range(0, vardim):
        temp=0
        for j in range(1,6):
            temp+=j*math.cos((j+1)*x[i]+j)
        s*=temp
    return s

def Matyas(vardim, x, bound):

    return 0.26*(x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]

def schwefel_s_problem_2_2(vardim, args, bound):
	X = np.array(args)
	X = np.abs(X)
	result = np.sum(X) + np.prod(X)
	# part_2 = np.cumprod(X)

	return result

def Bohachevsky(vardim, x, bound):
    a = x[0]**2
    b = 2*(x[1]**2)
    c = 0.3*(math.cos(3*math.pi*x[0]))
    d = 0.4*(math.cos(4*math.pi*x[1]))
    y = a + b - c - d + 0.7
    return y


def zakharov(vardim, x,bound):
    sum1 = 0
    sum2 = 0
    for i in range(vardim):
        sum1 = sum1 + (x[i]-1)**2
        sum2 = sum2 + 0.5*(i+1)*(x[i] -1)

    y = sum1 + sum2**2 + sum2**4
    return y

def levyN13(vardim, x, bound):
    term1 = (math.sin(3 * math.pi * x[0]))**2;
    term2 = ((x[0] - 1)**2) * (1 + math.sin(3 * math.pi * x[1])**2)
    term3 = ((x[1] - 1)**2) * (1 + math.sin(2 * math.pi * x[1])**2)

    y = term1 + term2 + term3
    return y


def sumSquares(vardim, x, bound):
    sum = 0.0
    for i in range(vardim):
        sum = sum + (x[i]*(i+1))**2

    return sum

def Holder_table(vardim, x, bound):
    fact1 = math.sin(x[0])*math.cos(x[1])
    fact2 = math.exp(math.fabs(1 - math.sqrt(x[0]**2 + x[1]**2)/math.pi))
    y = -math.fabs(fact1*fact2)
    return y

def Rosenbrock(vardim, x ,bound):
    sum = 0.0
    for i in range(vardim-1):
        fact1 = (x[i+1] - x[i])**2
        fact2 = (x[i] - 1)**2
        sum = 100* ((fact1)**2) + fact2
    return sum


def Beale(vardim, x, bound):
    term1 = (1.5 - x[0] + x[0]*x[1])**2
    term2 = (2.25 - x[0] + x[0]*(x[1])**2)**2
    term3 = (2.625 - x[0] + x[0]*(x[1])**3)**2

    y = term1 + term2 + term3

    return y

def Levy(vardim,x,bound):
    a=0
    pi = math.pi
    for i in range(0,vardim-1):
        a+=(x[i]-1)**2*(1+pow(math.sin(3*pi*x[i+1]),2))
    s=a+pow(math.sin(3*pi*x[0]),2)+abs(x[vardim-1]-1)*(1+pow(math.sin(3*pi*x[vardim-1]),2))
    return s

def Schwefel(vardim,x,bound):
    a=418.9829*vardim
    b=0
    for i in range(0, vardim):
        b+=x[i]*math.sin(math.sqrt(abs(x[i])))
    s=a-b
    return s