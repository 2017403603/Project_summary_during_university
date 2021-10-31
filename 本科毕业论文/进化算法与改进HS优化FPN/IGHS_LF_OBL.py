# coding=utf-8
# coding=utf-8
import time
import numpy as np
from HSIndividual import HSIndividual
import random
import copy
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
#从pyplot导入MultipleLocator类，这个类用于设置刻度间隔

class HarmonySearch:

    '''
    the class for harmony search algorithm
    '''

    def __init__(self, sizepop, vardim, bound, MAXGEN, params1, params2):
        '''
        sizepop: population sizepop
        vardim: dimension of variables
        bound: boundaries of variables
        MAXGEN: termination condition
        params1: algorithm required parameters, it is a list which is consisting of[HMCRmax,HMCRmin,PARmax,PARmin,bwmax,bwmin]
        [1.0,0.9,0.8,0.4,0.08,0.0008]
        params2 = [HMCR, PAR,bw]
        '''
        self.sizepop = sizepop
        self.vardim = vardim
        self.bound = bound
        self.MAXGEN = MAXGEN
        self.params1 = params1
        self.params2 = params2
        self.pm=0.005
        self.HMCR=0.9
        self.PAR=0.3
        self.BW=0.01
        self.population = []
        self.fitness = np.zeros((self.sizepop, 1))
        self.trace = np.zeros((self.MAXGEN, 4))
        self.best_harmony = []

    def initialize(self):
        '''
        initialize the population of hs
        '''
        for i in range(0, self.sizepop):
            ind = HSIndividual(self.vardim, self.bound, 0)
            ind.generate()
            self.population.append(ind)

    def evaluation(self):
        '''
        evaluation the fitness of the population
        '''
        for i in range(0, self.sizepop):
            self.population[i].calculateFitness()
            self.fitness[i] = self.population[i].fitness

    #0号
    def improvise(self):
        '''
        improvise a new harmony     即兴创作
        '''
        ind = HSIndividual(self.vardim, self.bound, 0)
        ind.chrom = np.zeros(self.vardim)
        worstIdx = np.argmax(self.fitness)
        bestIdx = np.argmin(self.fitness)
        for i in range(0, self.vardim):
            if random.random()<self.HMCR:
                xr = 2.0 * self.population[bestIdx].chrom[i] - self.population[worstIdx].chrom[i]
                if xr < self.bound[0, i]:
                    xr = self.bound[0, i]
                if xr > self.bound[1, i]:
                    xr = self.bound[1, i]
                ind.chrom[i] = self.population[worstIdx].chrom[i] + random.random() * (
                            xr - self.population[worstIdx].chrom[i])
                if random.random() <= self.pm:
                    ind.chrom[i] = self.bound[0, i] + \
                                   (self.bound[1, i] - self.bound[0, i]) * random.random()
            else:
                ind.chrom[i]=0.7*self.population[bestIdx].chrom[i] + 0.3*self.population[worstIdx].chrom[i]
                if random.random() < self.PAR:
                    ind.chrom[i] =ind.chrom[i]+random.random()*self.BW
            # r1 = random.random()
            # r2 = random.random()
            # if r1 <= self.params2[0]:
            #     if r2 < self.params2[1]:
            #         bestIdx = np.argmin(self.fitness)
            #         ind.chrom[i] = self.population[bestIdx].chrom[random.randint(0, self.vardim - 1)]
            #         # ind.chrom[i] += self.best.chrom[random.randint(0,self.vardim-1)]
            #     else:
            #         '''
            #         worstIdx = np.argmax(self.fitness)
            #         bestIdx = np.argmin(self.fitness)
            #         F1=min(self.population[bestIdx].chrom[i],self.population[worstIdx].chrom[i])
            #         F2=max(self.population[bestIdx].chrom[i],self.population[worstIdx].chrom[i])
            #         F=(F2-F1)/(2*F2-F1)
            #         ind.chrom[i] = self.population[worstIdx].chrom[i] + F * (
            #                     self.population[bestIdx].chrom[i] - self.population[worstIdx].chrom[i])
            #         '''
            #         bestIdx = np.argmin(self.fitness)
            #         ind.chrom[i] = self.population[bestIdx].chrom[i] + 0.6 * (
            #                     self.population[random.randint(0, self.sizepop - 1)].chrom[i] -
            #                     self.population[random.randint(0, self.sizepop - 1)].chrom[i])
            #         if ind.chrom[i] < self.bound[0, i]:
            #             ind.chrom[i] = self.bound[0, i]
            #         if ind.chrom[i] > self.bound[1, i]:
            #             ind.chrom[i] = self.bound[1, i]
            # else:
            #     ind.chrom[i] = self.population[random.randint(0, self.sizepop - 1)].chrom[i] + 0.6 * (
            #                 self.population[random.randint(0, self.sizepop - 1)].chrom[i] -
            #                 self.population[random.randint(0, self.sizepop - 1)].chrom[i])
            if ind.chrom[i] < self.bound[0, i]:
                ind.chrom[i] = self.bound[0, i]
            if ind.chrom[i] > self.bound[1, i]:
                ind.chrom[i] = self.bound[1, i]
        ind.calculateFitness()
        return ind

    def update(self, ind):
        '''
        update harmony memory
        '''
        maxIdx = np.argmax(self.fitness)
        #self.population[maxIdx] = ind
        #self.fitness[maxIdx] = ind.fitness
        if ind.fitness < self.population[maxIdx].fitness:
            # z = self.population[maxIdx].fitness
            # print("====更新和声库====")
            # print("在位置："+str(maxIdx)+"上更改")
            # print("解向量由：" + str(self.population[maxIdx].chrom) + "更改为：" +str(ind.chrom))
            # print("适应度函数由："+str(self.population[maxIdx].fitness)+"更改为："+str(ind.fitness))
            # print("=========")
            self.population[maxIdx] = ind
            self.fitness[maxIdx] = ind.fitness
            # print(z,"update","to",ind.fitness)

    def update1(self, ind):
        '''
        update harmony memory
        '''
        inf=1000000000000
        A = np.tile([inf], self.vardim)
        B = np.tile([-inf], self.vardim)
        for i in range(0,self.vardim):
            for j in range(0,self.sizepop):
                if A[i]>self.population[j].chrom[i]:
                    A[i]=self.population[j].chrom[i]
                if B[i]<self.population[j].chrom[i]:
                    B[i]=self.population[j].chrom[i]
        OV = HSIndividual(self.vardim, self.bound, 0)
        BV = HSIndividual(self.vardim, self.bound, 0)

        for i in range(0,self.vardim):
            k = random.random()
            OV.chrom[i]=k*(A[i]+B[i])-ind.chrom[i]
        OV.calculateFitness()
        if ind.fitness<OV.fitness:
            BV=ind
        else:
            BV=OV
        BV.calculateFitness()
        maxIdx = np.argmax(self.fitness)
        if BV.fitness < self.population[maxIdx].fitness:
            self.population[maxIdx] = BV
            self.fitness[maxIdx] = BV.fitness

    def updateparams(self):
        #if self.t < self.MAXGEN/2:
        #    self.params2[2] = self.params1[4]-(self.params1[4]-self.params1[5])/self.MAXGEN * ( self.t * 2)
        #else:
        #    self.params2[2] = self.params1[5]
        #self.params2[2] = self.params1[4] * math.exp(math.log(self.params1[5]/self.params1[4])/self.MAXGEN*self.t)
        self.params2[1] = self.params1[2]-(self.params1[2]-self.params1[3])/self.MAXGEN*self.t
        self.params2[0] = self.params1[1]+(self.params1[0]-self.params1[1])/self.MAXGEN*self.t
        #print("HMCR is %f,PAR is %f,BW is %f"%(self.params2[0],self.params2[1],self.params2[2]))

    def solve(self):
        '''
        the evolution process of the hs algorithm
        '''
        print("开始执行HS")
        start = time.time()
        self.t = 0
        self.initialize()
        self.evaluation()
        best = np.min(self.fitness)

        bestIndex = np.argmin(self.fitness)
        self.best = copy.deepcopy(self.population[bestIndex])
        self.avefitness = np.mean(self.fitness)
        self.stdev=np.std(self.fitness)
        #####
        worstIdx = np.argmax(self.fitness)
        self.worst = copy.deepcopy(self.population[worstIdx])
        ######
        #self.trace[self.t, 0] = (1 - self.best.fitness) / self.best.fitness
        #self.trace[self.t, 1] = (1 - self.avefitness) / self.avefitness
        self.trace[self.t, 0] = self.best.fitness
        self.trace[self.t, 1] = self.avefitness
        self.trace[self.t, 2] = self.worst.fitness
        self.trace[self.t, 3] = self.stdev
        while self.t < self.MAXGEN:
            self.updateparams()
            ind = self.improvise()
            self.update(ind)
            best = np.min(self.fitness)
            bestIndex = np.argmin(self.fitness)
            self.best = copy.deepcopy(self.population[bestIndex])
            self.best_harmony.append(self.best.chrom)
            self.avefitness = np.mean(self.fitness)
            self.stdev = np.std(self.fitness)
            worstIdx = np.argmax(self.fitness)
            self.worst = copy.deepcopy(self.population[worstIdx])
            # self.trace[self.t, 0] = (1 - self.best.fitness) / self.best.fitness
            # self.trace[self.t, 1] = (1 - self.avefitness) / self.avefitness
            self.trace[self.t, 0] = self.best.fitness
            self.trace[self.t, 1] = self.avefitness
            self.trace[self.t, 2] = self.worst.fitness
            self.trace[self.t, 3] = self.stdev
            self.t += 1
            # print("Generation %d: optimal function value is: %f; average function value is %f; worst function value is %f" % (
            #        self.t, self.trace[self.t, 0], self.trace[self.t, 1], self.trace[self.t, 2]))

        #print("Optimal function value is: %f; " % self.trace[self.t, 0])
        #print( "Optimal solution is:")
        #print ("x===",self.best.chrom)
        self.t-=1
        end = time.time()
        print("time:", end - start)
        print("IMGHSA_best:", self.best.fitness)
        print(self.trace[self.t])
        print("=================")

        #return self.best.fitness
        #self.printResult()

    def printResult(self):
        '''
        plot the result of abs algorithm
        '''
        x = np.arange(0, self.MAXGEN)
        y1 = self.trace[:, 0]
        y2 = self.trace[:, 1]
        y3 = self.trace[:, 2]
        plt.semilogy(x, y1, 'r', linestyle='--',label='optimal value')
        #plt.plot(x, y2, 'g', label='average value')
        #plt.plot(x, y3, 'b', label='worst value')
        #new_ticks = np.linspace(0, self.MAXGEN, 101)
        #plt.xticks(new_ticks)
        plt.xlabel("Iteration")
        plt.ylabel("function value")
        x_major_locator = MultipleLocator(50)
        # 把x轴的刻度间隔设置为1，并存在变量里
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(x_major_locator)
        # 把x轴的主刻度设置为5的倍数
        plt.xlim(0, 500)
        plt.ylim(1e-2,1e2)
        # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
        plt.title("Harmony search algorithm for function optimization")
        plt.legend()
        plt.show()