import numpy as np
from HSIndividual import HSIndividual
#from GSHS.HSIndividual2 import HSIndividual as HSIndividual2
import random
import copy
import math
import matplotlib.pyplot as plt
import time

class HarmonySearch:

    '''
    the class for harmony search algorithm
    '''

    def __init__(self, sizepop, vardim, bound, MAXGEN, params):
        '''
        sizepop: population sizepop
        vardim: dimension of variables
        bound: boundaries of variables
        MAXGEN: termination condition
        params: algorithm required parameters, it is a list which is consisting of[HMCR, PAR,bw]
        '''
        self.sizepop = sizepop
        self.vardim = vardim
        self.bound = bound
        self.MAXGEN = MAXGEN
        self.params = params
        self.population = []
        self.fitness = np.zeros((self.sizepop, 1))
        self.trace = np.zeros((self.MAXGEN, 4))

    def initialize(self):
        '''
        initialize the population of hs
        '''
        for i in range(0, self.sizepop):
            ind = HSIndividual(self.vardim, self.bound,0)
            ind.generate()
            self.population.append(ind)

    def evaluation(self):
        '''
        evaluation the fitness of the population   求解向量对应的解
        '''
        for i in range(0, self.sizepop):
            self.population[i].calculateFitness()
            self.fitness[i] = self.population[i].fitness

    def improvise(self):
        '''
        improvise a new harmony     即兴创作
        '''
        ind = HSIndividual(self.vardim, self.bound,0)
        # ind.chrom = np.zeros(self.vardim)
        # for i in range(0, self.vardim):
        #     if random.random() < self.params[0]:
        #         if random.random() < self.params[1]:
        #             ind.chrom[i] += self.best.chrom[i]
        #         else:
        #             worstIdx = np.argmin(self.fitness)
        #             xr = 2 * self.best.chrom[i] - \
        #                 self.population[worstIdx].chrom[i]
        #             if xr < self.bound[0, i]:
        #                 xr = self.bound[0, i]
        #             if xr > self.bound[1, i]:
        #                 xr = self.bound[1, i]
        #             ind.chrom[i] = self.population[worstIdx].chrom[
        #                 i] + (xr - self.population[worstIdx].chrom[i]) * random.random()
        #     else:
        #         ind.chrom[i] = self.bound[
        #             0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
        # ind.calculateFitness()
        # return ind

        for i in range(0,self.vardim):
            r1 = random.random()
            r2 = random.random()
            if r1 <=self.params[0]:
                if r2 <=self.params[1]:
                    if r2 > 0.5:
                        ind.chrom[i]=\
                        self.population[random.randint(0,self.sizepop-1)].chrom[i]+\
                            r2 *self.params[2]
                    else:
                        ind.chrom[i]=\
                        self.population[random.randint(0,self.sizepop-1)].chrom[i]-\
                            r2 *self.params[2]
                else:
                    ind.chrom[i]= \
                        self.population[random.randint(0, self.sizepop - 1)].chrom[i]

            else:
                ind.chrom[i] = self.bound[0, i] + \
                                (self.bound[1, i] - self.bound[0, i]) * random.random()

        ind.calculateFitness()
        return ind
    def improvise1(self):
        '''
        improvise a new harmony     即兴创作
        '''
        ind = HSIndividual(self.vardim, self.bound, 0)
        ind.chrom = np.zeros(self.vardim)

        for i in range(0, self.vardim):
            worstIdx = np.argmax(self.fitness)
            bestIdx = np.argmin(self.fitness)
            xr = 2 * self.population[bestIdx].chrom[i] - self.population[worstIdx].chrom[i]
            if xr < self.bound[0, i]:
                xr = self.bound[0, i]
            if xr > self.bound[1, i]:
                xr = self.bound[1, i]
            if random.random() < 0.5:
                ind.chrom[i] = self.population[worstIdx].chrom[i] + (
                        xr - self.population[worstIdx].chrom[i]) * random.random()
            else:
                ind.chrom[i] = self.population[worstIdx].chrom[i] - (
                        xr - self.population[worstIdx].chrom[i]) * random.random()
            if random.random() < 0.005:
                if random.random() < 0.5:
                    ind.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
                else:
                    ind.chrom[i] = self.bound[0, i] - (self.bound[1, i] - self.bound[0, i]) * random.random()

        ind.calculateFitness()
        return ind
    def update2(self, ind):
        '''
        update harmony memory
        '''
        maxIdx = np.argmax(self.fitness)
        self.population[maxIdx] = ind
        self.fitness[maxIdx] = ind.fitness
            # print(z,"update","to",ind.fitness)

    def update(self, ind):
        '''
        update harmony memory
        '''
        # minIdx = np.argmin(self.fitness)
        # if ind.fitness<self.population[minIdx].fitness:
        #     self.population[minIdx] = ind
        #     self.fitness[minIdx] = ind.fitness

        maxIdx = np.argmax(self.fitness)
        if ind.fitness < self.population[maxIdx].fitness:
            #z = self.population[maxIdx].fitness
            # print("====更新和声库====")
            # print("在位置："+str(maxIdx)+"上更改")
            # print("解向量由：" + str(self.population[maxIdx].chrom) + "更改为：" +str(ind.chrom))
            # print("适应度函数由："+str(self.population[maxIdx].fitness)+"更改为："+str(ind.fitness))
            # print("=========")
            self.population[maxIdx] = ind
            self.fitness[maxIdx] = ind.fitness

            #print(z,"update","to",ind.fitness)



    def solve(self):
        '''
        the evolution process of the hs algorithm
        '''
        print("开始执行HS")
        start = time.time()
        self.t = 0
        self.initialize()
        self.evaluation()

        bestIndex = np.argmin(self.fitness)
        self.best = copy.deepcopy(self.population[bestIndex])
        self.avefitness = np.mean(self.fitness)
        self.stdev = np.std(self.fitness)
        worstIdx = np.argmax(self.fitness)
        worst = copy.deepcopy(self.population[worstIdx])


        self.trace[self.t,0] = self.best.fitness
        self.trace[self.t,1] = self.avefitness
        self.trace[self.t,2] = worst.fitness
        self.trace[self.t, 3] = self.stdev
        # print("Generation %d: optimal function value is: %f; average function value is %f" % (
        #     self.t, self.trace[self.t, 0], self.trace[self.t, 1]))
        # print("====当前最小值====")
        # print(self.trace[self.t, 0])
        # print("====当前最大值====")
        # print(self.trace[self.t, 2])
        # print("========")
        while self.t < self.MAXGEN - 1 :
            #print("执行次数为：",self.t)
            if(self.best.fitness!=0.000):
                self.t += 1
                ind1 = self.improvise()
                self.update(ind1)

            # best = np.max(self.fitness)
            # bestIndex = np.argmin(self.fitness)
            # if best >self.best.fitness:
            #     self.best = copy.deepcopy(self.population[bestIndex])

            # best = np.min(self.fitness)
            # bestIndex = np.argmin(self.fitness)
            # if best < self.best.fitness:
            #     self.best = copy.deepcopy(self.population[bestIndex])
            # self.avefitness = np.mean(self.fitness)

            # self.trace[self.t, 0] = (1 - self.best.fitness) / self.best.fitness
            # self.trace[self.t, 1] = (1 - self.avefitness) / self.avefitness

                bestIndex = np.argmin(self.fitness)
                self.best = self.population[bestIndex]
                self.avefitness = np.mean(self.fitness)
                self.stdev = np.std(self.fitness)
                worstIdx = np.argmax(self.fitness)
                worst = copy.deepcopy(self.population[worstIdx])

                self.trace[self.t, 0] = self.best.fitness
                self.trace[self.t, 1] = self.avefitness
                self.trace[self.t, 2] = worst.fitness
                self.trace[self.t, 3] = self.stdev
                # print("====当前最小值====")
                # print(self.trace[self.t, 0])
                # print("====当前最大值====")
                # print(self.trace[self.t, 2])
                # print("========")
                # print("Generation %d: optimal function value is: %f; average function value is %f" % (
                #     self.t, self.trace[self.t, 0], self.trace[self.t, 1]))
            else:
                print("rate:", self.t)
                break
        # print("Optimal function value is: %f; " % self.trace[self.t, 0])
        # print("Optimal solution is:")
        # for i in range(self.sizepop):
        #     print(self.population[i].chrom,self.population[i].fitness)
        #print("返回最好的和声：",self.best.chrom)
        #np.save('C:/Users/ASUS/Desktop/最好和声（BP神经网络初始化权重）',self.best.chrom)
        end = time.time()
        print("time:",end-start)
        print("HS_best:",self.best.fitness)
        print("=================")
        print(self.trace[self.t])

        #self.printResult()

    def printResult(self):
        '''
        plot the result of abs algorithm
        '''
        x = np.arange(0, self.MAXGEN)
        y1 = self.trace[:, 0]
        y2 = self.trace[:, 1]
        plt.plot(x, y1, 'r', label='optimal value')
        plt.plot(x, y2, 'g', label='average value')
        plt.xlabel("Iteration")
        plt.ylabel("function value")
        plt.title("Harmony search algorithm for function optimization")
        plt.legend()
        plt.show()