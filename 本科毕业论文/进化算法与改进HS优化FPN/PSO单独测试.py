# coding=utf-8
import numpy as np
from matplotlib.ticker import MultipleLocator
from sko.GA import GA
from sko.DE import DE
from sko.PSO import PSO
from sko.ACA import ACA_TSP
import pandas as pd
import matplotlib.pyplot as plt
import IGHS_LF_OBL
from Fuzzy_petri_net import Fuzzy_petri_net

#计算适应度函数
def calculateFPNFitness(P):
    chrom=P
    temp = Fuzzy_petri_net()
    fitness = temp.MSE(chrom)
    return fitness

#打印FPN参数
def PrintFPNparameter(bestChrom):
    train_data = np.load("随机生成的样本数据.npy")
    train_data.tolist()
    temp = Fuzzy_petri_net()
    for i in range(0, len(train_data)):
        temp.init(bestChrom, i, train_data)
        #print("第", i, "组测试结果：")
        temp.hope_FPN_caculate()
        temp.real_FPN_caculate()
    print("w1=", temp.w1, "w2=", temp.w2, "w3=", temp.w3, "w4=", temp.w4, "w5=", temp.w5)
    print("u1=", temp.u1, "u2=", temp.u2, "u3=", temp.u3, "u4=", temp.u4, "u5=", temp.u5)
    print("t1=", temp.t1, "t2=", temp.t2, "t3=", temp.t3, "t4=", temp.t4, "t5=", temp.t5)


if __name__ == '__main__':
    # 初始化FPN参数
    # 上下边界定义
    temp_lb = []
    temp_ub = []
    for i in range(0, 15):
        temp_lb.append(0)
        temp_ub.append(1)
    # 函数维度
    vardim = 15
    # 迭代次数
    iterate = 2500
    ######################
    # 运行PSO+FPN
    pso = PSO(func=calculateFPNFitness, n_dim=vardim, pop=40, max_iter=iterate, lb=temp_lb, ub=temp_ub, w=0.8, c1=0.5,
              c2=0.50)
    pso.record_mode = True
    pso.run()
    print('PSO迭代完成最优解:', pso.gbest_x, '\n', 'PSO迭代完成最小适应度:', pso.gbest_y)
    print('以下为PSO优化FPN参数的结果：')
    PrintFPNparameter(pso.gbest_x)
    # 保存数据
    np.save("特例PSO参数优化Fitness.npy", pso.gbest_y_hist)
    np.save("特例PSO+FPN最优个体集合.npy", pso.gbest_x)
    plt.semilogy(np.arange(0, len(pso.gbest_y_hist)), pso.gbest_y_hist, 'k', linestyle='--', label='PSO+FPN',
                 marker='s', markevery=250, linewidth=1.0)

    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 22,
            }
    plt.xlabel("iteration", font)
    plt.ylabel("Fitness", font)
    x_major_locator = MultipleLocator(500)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.xlim(0, 2500)
    # plt.ylim(1e-8, 1e0)
    plt.title("Experimental comparison")
    plt.legend(fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=15)
    plt.show()