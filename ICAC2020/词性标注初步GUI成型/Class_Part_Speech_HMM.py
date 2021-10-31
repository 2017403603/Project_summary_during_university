#!usr/bin/python3
#encoding = 'utf-8'
import operator
import os,sys,jieba
import re

class miaowenHMM:

    def __init__(self):
        self.inputData = ''#输入数据
        self.partData = []#分词结果
        self.partDataInformation = []#分词信息
        self.partNominalInformation = []#语法信息

        def readPartSpecch():  # 读取所含的隐含状态信息
            f = open('cixing.txt', 'r')
            line = f.readline()
            # global state_list
            state_list = []
            while line:
                state_list.append(str(re.findall(r'[a-zA-Z]+', line)).replace("['", '').replace("']", ''))
                line = f.readline()
            # print(state_list)
            # print(state_list.__len__())
            return state_list
        def load_Model(f_name):
            ifp = open(f_name, 'rb')
            return eval(ifp.read())

        self.prob_start = load_Model("B_prob_start.py")
        self.prob_trans = load_Model("B_prob_trans.py")
        self.prob_emit = load_Model("B_prob_emit.py")
        self.state_list = readPartSpecch()

    def getIntputData(self):
        return self.inputData

    def setIntputData(self,sentence):
        self.inputData = sentence

    def getPartData(self):
        return self.partData

    def setIntputData(self,sentencePartData):
        self.inputData = sentencePartData

    def getPartData(self):
        return self.partData

    def setPartDataInformation(self,sentencePartDataInformation):
        self.inputData = sentencePartDataInformation

    def getPartNominalInformation(self):
        return self.partData

    def setPartNominalInformation(self,sentencePartNominalInformation):
        self.inputData = sentencePartNominalInformation


    def viterbi(self,obs, states, start_p, trans_p, emit_p):
        # print(states)
        V = [{}]  # tabular
        path = {}
        for y in states:
            V[0][y] = start_p[y] * emit_p[y].get(obs[0], 0)
            path[y] = y
            # print(V[0][y])
        for t in range(1, len(obs)):
            V.append({})
            newpath = {}
            for y in states:
                # print(obs[t])
                (prob, state) = max(
                    [(V[t - 1][y0] * trans_p[y0].get(y, 0), y0) for y0 in states if V[t - 1][y0] > 0],
                    # default=(max([(trans_p[y0].get(y, 0), y0) for y0 in states]))
                    default=(0, 'x')
                    # default=(max([(trans_p[y0].get(y, 0) * emit_p[y].get(obs[t], 0), y0) for y0 in states]))
                )

                # default = (max([(trans_p[y0].get(y, 0) * emit_p[y].get(obs[t], 0), y0) for y0 in states]))
                # 以上代码是尝试解决未登陆词问题，还未找到解决办法
                # if(emit_p[y].get(obs[t], 0)>0):
                V[t][y] = prob * emit_p[y].get(obs[t], 0)
                # else:
                # V[t][y] = prob
                newpath[y] = path[state] + ' ' + y
            path = newpath
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
        return (prob, path[state])

    def Part_of_Speech(self,sentence):
        """
        用viterbi算法将sentence这个已分词的列表进行词性标注
        :param sentence:
         已分好词的句子List
        :return: 
        pos_list：状态字符串
        prob：当前这个状态序列的概率
        """
        # pdb.set_trace()
        #prob,pos_list = self.viterbi()
        prob, pos_list = self.viterbi(sentence, self.state_list, self.prob_start,self. prob_trans, self.prob_emit)
        return (prob, pos_list)
