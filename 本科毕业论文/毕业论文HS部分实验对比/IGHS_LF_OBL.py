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
        self.population = []
        self.fitness = np.zeros((self.sizepop, 1))
        self.trace = np.zeros((self.MAXGEN, 4))

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

    def levy_flight(self, Lambda=1.5):
        # generate step from levy distribution
        sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) \
                          / math.gamma((1 + Lambda) / 2) * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
        sigma2 = 1
        u = np.random.normal(0, sigma1, size=self.vardim)
        v = np.random.normal(0, sigma2, size=self.vardim)
        # np.fabs(v)取V元素的绝对值
        step = u / np.power(np.fabs(v), 1 / Lambda)
        return step
    #0号
    def update(self, ind):
        '''
        update harmony memory
        '''
        maxIdx = np.argmax(self.fitness)
        if ind.fitness < self.population[maxIdx].fitness:
            self.population[maxIdx] = ind
            self.fitness[maxIdx] = ind.fitness
    def improvise(self):
        lhc_levy = self.levy_flight(1.5)
        ind = HSIndividual(self.vardim, self.bound, 0)
        ind.chrom = np.zeros(self.vardim)
        for i in range(0, self.vardim):
            worstIdx = np.argmax(self.fitness)
            bestIdx = np.argmin(self.fitness)
            r1 = random.random()
            r2 = random.random()
            if r1 <= self.params2[0]:
                if r2 < self.params2[1]:
                    ind.chrom[i] = self.population[bestIdx].chrom[random.randint(0, self.vardim - 1)]
                else:
                    ind.chrom[i] = self.population[worstIdx].chrom[i] + 0.6 *(
                            self.population[bestIdx].chrom[i] - self.population[worstIdx].chrom[i])
                if ind.chrom[i] < self.bound[0, i] or ind.chrom[i] > self.bound[1, i]:
                    ind.chrom[i]=self.bound[0, i]+(self.bound[1, i]-self.bound[0, i])*random.random()
            else:
                ind.chrom[i] = self.population[random.randint(0, self.sizepop - 1)].chrom[i] + lhc_levy[i] * 0.01* (
                            self.population[random.randint(0, self.sizepop - 1)].chrom[i] -
                            self.population[random.randint(0, self.sizepop - 1)].chrom[i])
                if ind.chrom[i] < self.bound[0, i] or ind.chrom[i] > self.bound[1, i]:
                    ind.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
        ind.calculateFitness()
        return ind
    def second_levy_improvise(self):
        worstIdx = np.argmax(self.fitness)
        bestIdx = np.argmin(self.fitness)
        levy_ind_best = HSIndividual(self.vardim, self.bound, 0)
        levy_ind_worst = HSIndividual(self.vardim, self.bound, 0)
        lhc_levy = self.levy_flight(1.5)
        for i in range(0, self.vardim):
            levy_ind_best.chrom[i] = -self.population[bestIdx].chrom[i]+ lhc_levy[i] * 0.001*(self.population[bestIdx].chrom[i] - \
                        self.population[worstIdx].chrom[i])
            levy_ind_worst.chrom[i] = -self.population[worstIdx].chrom[i]+ lhc_levy[i] * 0.01*(self.population[bestIdx].chrom[i] - \
                        self.population[worstIdx].chrom[i])
            if levy_ind_best.chrom[i] < self.bound[0, i] or levy_ind_best.chrom[i] > self.bound[1, i]:
                levy_ind_best.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
            if levy_ind_worst.chrom[i] < self.bound[0, i] or levy_ind_worst.chrom[i] > self.bound[1, i]:
                levy_ind_worst.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
        levy_ind_best.calculateFitness()
        levy_ind_worst.calculateFitness()
        self.update(levy_ind_best)
        self.update(levy_ind_worst)
    def second_OBL_improvise(self,ind):
        worstIdx = np.argmax(self.fitness)
        bestIdx = np.argmin(self.fitness)
        new_ind = HSIndividual(self.vardim, self.bound, 0)
        for i in range(0, self.vardim):
            new_ind.chrom[i]=(self.population[bestIdx].chrom[i]+self.population[worstIdx].chrom[i])-ind.chrom[i]
        new_ind.calculateFitness()
        self.update(new_ind)
    def second_OBL_best_improvise(self):
        inf = 1000000000000
        A = np.tile([inf], self.vardim)
        B = np.tile([-inf], self.vardim)
        for i in range(0, self.vardim):
            for j in range(0, self.sizepop):
                if A[i] > self.population[j].chrom[i]:
                    A[i] = self.population[j].chrom[i]
                if B[i] < self.population[j].chrom[i]:
                    B[i] = self.population[j].chrom[i]
        OBL_X_best=HSIndividual(self.vardim, self.bound, 0)
        OBL_X_worst = HSIndividual(self.vardim, self.bound, 0)
        bestIdx = np.argmin(self.fitness)
        worstIdx = np.argmax(self.fitness)
        for i in range(0, self.vardim):
            OBL_X_best.chrom[i] = random.random()*(A[i] + B[i]) - self.population[bestIdx].chrom[i]
            OBL_X_worst.chrom[i] = random.random()*(A[i] + B[i]) - self.population[worstIdx].chrom[i]
            if OBL_X_best.chrom[i] < self.bound[0, i] or OBL_X_best.chrom[i] > self.bound[1, i]:
                OBL_X_best.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
            if OBL_X_worst.chrom[i] < self.bound[0, i] or OBL_X_worst.chrom[i] > self.bound[1, i]:
                OBL_X_worst.chrom[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * random.random()
        OBL_X_best.calculateFitness()
        OBL_X_worst.calculateFitness()
        # if OBL_X.fitness < self.population[bestIdx].fitness:
        #     self.population[bestIdx] = OBL_X
        #     self.fitness[bestIdx] = OBL_X.fitness
        # else:
        #     temp_k=random.randint(0, self.sizepop - 1)
        #     self.population[temp_k] = OBL_X
        #     self.fitness[temp_k] = OBL_X.fitness
        self.update(OBL_X_worst)
        self.update(OBL_X_best)
    def product_chao(self):
        for i in range(0,10000):
            temp=random.random()
            if temp!=0 and temp!=0.25 and temp!=0.5 and temp!=0.75 and temp!=1.0:
                return temp
    def second_chaos_improvise(self):
        chao_y = np.tile([0.0], self.vardim)
        r_gn = np.tile([0.0], self.vardim)
        chao_y[0]=self.product_chao()
        for i in range(1,self.vardim):
            chao_y[i]=4.0*chao_y[i-1]*(1-chao_y[i-1])
        for i in range(0,self.vardim):
            r_gn[i]=random.random()*(1.0-1.0/(1+math.exp(-0.02*self.t+4)))
        bestIdx = np.argmin(self.fitness)
        chao_ind=HSIndividual(self.vardim, self.bound, 0)
        for i in range(0,self.vardim):
            chao_ind.chrom[i]=-self.population[bestIdx].chrom[i]+r_gn[i]*(2.0*chao_y[i]-1)
        chao_ind.calculateFitness()
        return chao_ind

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
        self.update(BV)
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
        while self.t < self.MAXGEN - 1:
            self.t += 1
            self.updateparams()
            ind = self.improvise()
            self.update(ind)
            self.second_OBL_best_improvise()
            #chao_ind=self.second_chaos_improvise()
            #self.update(chao_ind)

            best = np.min(self.fitness)
            bestIndex = np.argmin(self.fitness)
            self.best = copy.deepcopy(self.population[bestIndex])
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
            # print("Generation %d: optimal function value is: %f; average function value is %f; worst function value is %f" % (
            #        self.t, self.trace[self.t, 0], self.trace[self.t, 1], self.trace[self.t, 2]))

        #print("Optimal function value is: %f; " % self.trace[self.t, 0])
        #print( "Optimal solution is:")
        print ("x===",self.best.chrom)
        end = time.time()
        print("time:", end - start)
        print("IGHS-LF-OBL_best:", self.best.fitness)
        print(self.trace[self.t])
        print("=================")

