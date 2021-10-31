# coding=utf-8
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.ticker import MultipleLocator
#IGHS-LF-OBL
import GOGHS
import HS
import IDHS
import matplotlib.pyplot as plt
import scipy.io as sio
from pylab import mpl
import IGHS_LF_OBL
import ID_HS_LDD
import IMGHSA
import NGHS

if __name__ == "__main__":
     idhs_list=[]
     hs_list=[]
     nghs_list = []
     goghs_list = []
     idhsldd_list = []
     imghsa_list = []
     ighslfobl_list = []
     for ll in range(0,30):
          print("第",ll,"次：")
          vardim = 50
          bound = np.tile([[-100.0], [100.0]], vardim)
          iterate = 3000
          #################
          idhs = IDHS.HarmonySearch(20, vardim, bound, iterate, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                    [0.9950, 0.4, 0.0008])
          idhs.solve()
          hs = HS.HarmonySearch(5, vardim, bound, iterate, [0.9, 0.3, 0.001])
          hs.solve()
          nghs = NGHS.HarmonySearch(5, vardim, bound, iterate, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                    [0.9950, 0.4, 0.0008])
          nghs.solve()
          goghs = GOGHS.HarmonySearch(5, vardim, bound, iterate, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                      [0.9950, 0.4, 0.0008])
          goghs.solve()
          id_hs_ldd = ID_HS_LDD.HarmonySearch(30, vardim, bound, iterate, [0.99, 0.3, 0.99, 0.9, 0.0008, 0.00008],
                                              [0.9950, 0.4, 0.0008])
          id_hs_ldd.solve()
          imghsa = IMGHSA.HarmonySearch(30, vardim, bound, iterate, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                       [0.9950, 0.4, 0.0008])
          imghsa.solve()
          ighslfobl = IGHS_LF_OBL.HarmonySearch(5, vardim, bound, iterate, [0.9, 0.8, 0.9, 0.1, 0.0008, 0.00008],
                                                [0.9950, 0.4, 0.0008])
          ighslfobl.solve()
          #################
          x = np.arange(0, idhs.MAXGEN)
          idhs_y = idhs.trace[:, 0]
          hs_y = hs.trace[:, 0]
          nghs_y = nghs.trace[:, 0]
          goghs_y = goghs.trace[:, 0]
          id_hs_ldd_y = id_hs_ldd.trace[:, 0]
          imghsa_y = imghsa.trace[:, 0]
          ighslfobl_y = ighslfobl.trace[:, 0]
          #################
          plt.semilogy(x, hs_y, 'k', linestyle=':', label='HS', marker='*', markevery=120, linewidth=1.0)
          plt.semilogy(x, nghs_y, 'y', linestyle='-.', label='NGHS', marker='>', markevery=120, linewidth=1.0)
          plt.semilogy(x, goghs_y, 'c', linestyle='--', label='GOGHS', marker='D', markevery=120, linewidth=1.0)
          plt.semilogy(x, idhs_y, 'b', linestyle='--', label='IDHS', marker='^', markevery=120, linewidth=1.0)
          plt.semilogy(x, id_hs_ldd_y, 'g', linestyle=':', label='ID-HS-LDD', marker='s', markevery=120, linewidth=1.0)
          plt.semilogy(x, imghsa_y, 'm', linestyle='-.', label='IMGHSA', marker='v', markevery=120, linewidth=1.0)
          plt.semilogy(x, ighslfobl_y, 'r', linestyle='-', label='IGHS-LF-OBL', marker='o', markevery=120,
                       linewidth=1.0)
          #########################
          # plt.plot(x, hs_y, 'k', linestyle=':', label='HS', marker='*', markevery=120, linewidth=1.0)
          # plt.plot(x, nghs_y, 'y', linestyle='-.', label='NGHS', marker='>', markevery=120, linewidth=1.0)
          # plt.plot(x, goghs_y, 'c', linestyle='--', label='GOGHS', marker='D', markevery=120, linewidth=1.0)
          # plt.plot(x, idhs_y, 'b', linestyle='--', label='IDHS', marker='^', markevery=120, linewidth=1.0)
          # plt.plot(x, id_hs_ldd_y, 'g', linestyle=':', label='ID-HS-LDD', marker='s', markevery=120, linewidth=1.0)
          # plt.plot(x, imghsa_y, 'm', linestyle='-.', label='IMGHSA', marker='v', markevery=120, linewidth=1.0)
          # plt.plot(x, ighslfobl_y, 'r', linestyle='-', label='IGHS-LF-OBL', marker='o', markevery=120,
          #              linewidth=1.0)
          #########################
          font = {'family': 'Times New Roman',
                  'weight': 'normal',
                  'size': 22,
                  }
          plt.xlabel("iteration", font)
          plt.ylabel("function value", font)
          x_major_locator = MultipleLocator(300)
          ax = plt.gca()
          plt.xlim(0, 3000)
          plt.ylim(1e-70, 1e4)
          #plt.ylim(-210,100)
          # plt.title("Experimental comparison")
          # plt.legend(fontsize=15)
          plt.xticks(fontsize=12)
          plt.yticks(fontsize=15)
          plt.show()

          idhs_list.append(idhs.trace[-1,0])
          hs_list.append(hs.trace[-1,0])
          nghs_list.append(nghs.trace[-1, 0])
          goghs_list.append(goghs.trace[-1, 0])
          idhsldd_list.append(id_hs_ldd.trace[-1, 0])
          imghsa_list.append(imghsa.trace[-1, 0])
          ighslfobl_list.append(ighslfobl.trace[-1, 0])

     print("平均值为：",np.mean(idhs_list),"方差为：",np.std(idhs_list))
     print("平均值为：", np.mean(hs_list), "方差为：", np.std(hs_list))
     print("平均值为：", np.mean(nghs_list), "方差为：", np.std(nghs_list))
     print("平均值为：", np.mean(goghs_list), "方差为：", np.std(goghs_list))
     print("平均值为：", np.mean(idhsldd_list), "方差为：", np.std(idhsldd_list))
     print("平均值为：", np.mean(imghsa_list), "方差为：", np.std(imghsa_list))
     print("平均值为：", np.mean(ighslfobl_list), "方差为：", np.std(ighslfobl_list))

