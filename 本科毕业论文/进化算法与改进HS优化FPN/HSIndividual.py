# coding=utf-8
# coding=utf-8
import numpy as np

import random
from Fuzzy_petri_net import Fuzzy_petri_net
'''
generate a solution vector
'''

class HSIndividual:

    '''
    individual of harmony search algorithm
    '''

    def __init__(self,  vardim, bound , n):
        '''
        vardim: dimension of variables
        bound: boundaries of variables
        '''
        self.vardim = vardim
        self.bound = bound
        self.n = n
        self.chrom = np.zeros(self.vardim)
        self.fitness = 0.

    def generate(self):
        '''
        generate a random chromsome for harmony search algorithm
        '''

        #rnd = np.random.random(size=self.vardim)

        for i in range(0, self.vardim):

            self.chrom[i] = self.bound[0, i] + \
                (self.bound[1, i] - self.bound[0, i]) * random.random()

    def calculateFitness(self):
        '''
        calculate the fitness of the chromsome
        '''
        temp = Fuzzy_petri_net()
        self.fitness = temp.MSE(self.chrom)
        #self.fitness = ObjFunction.Sphere(self.vardim, self.chrom, self.bound)