# coding=utf-8
import random

import numpy as np


class Fuzzy_petri_net():
      def init(self,chrom,test,input_list):
          ###########################################
          self.w1_standard = 0.2;self.w2_standard = 0.5;self.w3_standard = 0.3;self.w4_standard = 0.4;self.w5_standard = 0.6
          self.u1_standard = 0.7;self.u2_standard = 0.9;self.u3_standard = 0.6;self.u4_standard = 0.8;self.u5_standard = 0.7
          self.t1_standard = 0.3;self.t2_standard = 0.4;self.t3_standard = 0.2;self.t4_standard = 0.5;self.t5_standard = 0.4
          ###########################################
          self.w1 = chrom[0];self.w2 = chrom[1];self.w3 = chrom[2];self.w4 = chrom[3];self.w5 = chrom[4]
          self.u1 = chrom[5];self.u2 = chrom[6];self.u3 = chrom[7];self.u4 = chrom[8];self.u5 = chrom[9]
          self.t1 = chrom[10];self.t2 = chrom[11];self.t3 = chrom[12];self.t4 = chrom[13];self.t5 = chrom[14]
          sum1=self.w1 + self.w2 + self.w3;sum2=self.w4 + self.w5
          if sum1==0.0:
              sum1+=1e-10
          if sum2==0.0:
              sum2+=1e-10
          self.w1=self.w1*1.0/sum1;self.w2=self.w2*1.0/sum1;self.w3=self.w3*1.0/sum1;self.w4=self.w4*1.0/sum2;self.w5=self.w5*1.0/sum2;
          ###########################################
          self.input_list = input_list
          # self.input_list =[[0.9, 0.9, 0.9, 0.9], [0.2, 0.8, 0.5, 0.8], [0.4, 0.7, 0.6, 0.7],
          #  [0.8, 0.4, 0.2, 0.9], [0.9, 0.5, 0.4, 0.9], [0.3, 0.7, 0.5, 0.9]]
          self.p1=self.input_list[test][0];self.p4=self.input_list[test][1];self.p5=self.input_list[test][2];self.p7=self.input_list[test][3]
          # self.p1 = 0.3+(1.0-0.3)*random.random()
          # self.p4 = 0.3+(1.0-0.3)*random.random()
          # self.p5 = 0.3+(1.0-0.3)*random.random()
          # self.p7 = 0.3+(1.0-0.3)*random.random()

      def fuzzy_reason_function(self,x,k):
          if x>k:            #===========
              return 1.0*x
          else:
              return 0.0
          #return 1.0/(1.0+np.exp(-50000*(x-k)))*x
      def max_caculate_con_function(self,x1,x2):
          return max(x1,x2)
          # return x1/(1.0+np.exp(-50000*(x1-x2)))+x2/(1.0+np.exp(-50000*(x2-x1)))
      def hope_FPN_caculate(self):
          ###第一层
          x1=self.fuzzy_reason_function(self.p1*self.u1_standard,self.t1_standard)
          p2=self.fuzzy_reason_function(self.p1*self.u2_standard,self.t2_standard)
          ###第二层
          x2=self.fuzzy_reason_function(p2*self.u3_standard,self.t3_standard)
          p3=self.max_caculate_con_function(x1,x2)
          ###第三层
          x3=self.p4*self.w1_standard+p3*self.w2_standard+self.p5*self.w3_standard
          p6=self.fuzzy_reason_function(x3*self.u4_standard,self.t4_standard)
          ###第四层
          x4=p6*self.w4_standard+self.p7*self.w5_standard
          p8=self.fuzzy_reason_function(x4*self.u5_standard,self.t5_standard)
          #print("hope_p8=:",p8)
          return p8
      def real_FPN_caculate(self):
          ###第一层
          x1 = self.fuzzy_reason_function(self.p1 * self.u1, self.t1)
          p2 = self.fuzzy_reason_function(self.p1 * self.u2, self.t2)
          ###第二层
          x2 = self.fuzzy_reason_function(p2 * self.u3, self.t3)
          p3 = self.max_caculate_con_function(x1, x2)
          ###第三层
          x3 = self.p4 * self.w1 + p3 * self.w2 + self.p5 * self.w3
          p6 = self.fuzzy_reason_function(x3 * self.u4, self.t4)
          ###第四层
          x4 = p6 * self.w4 + self.p7 * self.w5
          p8 = self.fuzzy_reason_function(x4 * self.u5, self.t5)
          #print("real_p8=:", p8)
          return p8
      def MSE(self,chrom):
          input_list = np.load("随机生成的样本数据.npy")
          input_list.tolist()
          sum_mse=0.0
          for test in range(0,len(input_list)):
              self.init(chrom,test,input_list)
              hope = self.hope_FPN_caculate()
              real = self.real_FPN_caculate()
              sum_mse+=(hope-real)*(hope-real)*0.5
          return sum_mse
