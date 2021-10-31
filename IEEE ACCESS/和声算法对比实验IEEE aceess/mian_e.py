# coding=utf-8
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.ticker import MultipleLocator
import my_HS
import sci_HS
import HSDM_HS
import ID_HS_LDD_HS
import matplotlib.pyplot as plt
import scipy.io as sio
from pylab import mpl
if __name__ == "__main__":
     for ll in range(0,5):
          print("第",ll,"次：")
          vardim = 30
          bound = np.tile([[-10.0], [10.0]], vardim)
          ###################
          my_hs = my_HS.HarmonySearch(5, vardim, bound, 5000, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                      [0.9950, 0.4, 0.0008])
          my_hs.solve()
          #################
          sci_hs = sci_HS.HarmonySearch(20, vardim, bound, 5000, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                        [0.9950, 0.4, 0.0008])
          sci_hs.solve()
          #################
          HSDM_hs = HSDM_HS.HarmonySearch(50, vardim, bound, 5000, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                          [0.9950, 0.4, 0.0008])
          HSDM_hs.solve()
          #################
          ID_HS_LDD_hs = ID_HS_LDD_HS.HarmonySearch(30, vardim, bound, 5000, [0.99, 0.3, 0.99, 0.9, 0.0008, 0.00008],
                                                    [0.98, 0.4, 0.0008])
          ID_HS_LDD_hs.solve()
          #################
          x = np.arange(0, my_hs.MAXGEN)
          myHS_y = my_hs.trace[:, 0]
          sciHS_y = sci_hs.trace[:, 0]
          HSDM_y = HSDM_hs.trace[:, 0]
          ID_HS_LDD_y = ID_HS_LDD_hs.trace[:, 0]
          ######################
          # 坐标轴的刻度设置向内(in)或向外(out)
          plt.rcParams['xtick.direction'] = 'in'
          plt.rcParams['ytick.direction'] = 'in'
          ######################

          plt.semilogy(x, myHS_y, 'r', linestyle='-', label='AGOHS',linewidth=2.0)
          plt.semilogy(x, sciHS_y, 'b', linestyle='--', label='IDHS',linewidth=2.0)
          plt.semilogy(x, HSDM_y, 'k', linestyle='-.', label='HSDM',linewidth=2.0)
          plt.semilogy(x, ID_HS_LDD_y, 'g', linestyle=':', label='ID-HS-LDD',linewidth=2.0)

          # plt.plot(x, myHS_y, 'r', linestyle='-', label='AGOHS', linewidth=2.0)
          # plt.plot(x, sciHS_y, 'b', linestyle='--', label='IDHS', linewidth=2.0)
          # plt.plot(x, HSDM_y, 'k', linestyle='-.', label='HSDM', linewidth=2.0)
          # plt.plot(x, ID_HS_LDD_y, 'g', linestyle=':', label='ID-HS-LDD', linewidth=2.0)
          #########################
          font = {'family': 'FangSong',
                  'weight': 'normal',
                  'size': 18,
                  }
          plt.xlabel("迭代次数", font)
          plt.ylabel("最优和声函数值", font)
          x_major_locator = MultipleLocator(500)
          ax = plt.gca()
          ax.xaxis.set_major_locator(x_major_locator)
          plt.xlim(0, 5000)
          plt.ylim(10e-101, 10e3)
          plt.yticks([10e-101, 10e-86, 10e-67, 10e-56, 10e-45, 10e-34, 10e-23, 10e-12, 10e2])
          #plt.yticks([10e-201, 10e-171, 10e-141, 10e-111, 10e-81,10e-51,10e-21,10e1])
          # plt.title("Experimental comparison")
          #plt.legend(fontsize=15)
          plt.xticks(fontsize=12)
          plt.yticks(fontsize=15)
          # Hide the right and top spines
          ax.spines['right'].set_visible(False)
          ax.spines['top'].set_visible(False)
          plt.show()
