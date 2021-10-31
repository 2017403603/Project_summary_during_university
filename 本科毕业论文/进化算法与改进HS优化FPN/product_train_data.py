# coding=utf-8
import random
import numpy as np
if __name__ == "__main__":
    train_data=[]
    for i in range(0,20):
        temp=[]
        for j in range(0,4):
            r=0.0+(1.0-0.0)*random.random()
            r=round(r, 1)
            temp.append(r)
        train_data.append(temp)

    for i in range(0,30):
        temp=[]
        for j in range(0,4):
            r=0.0+(1.0-0.0)*random.random()
            r=round(r, 1)
            temp.append(r)
        train_data.append(temp)
    np.array(train_data)
    print(train_data)
    print(len(train_data))
    np.save("随机生成的样本数据.npy",train_data)
    #input_list = np.load("随机生成的样本数据.npy")
