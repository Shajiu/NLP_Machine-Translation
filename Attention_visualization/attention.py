#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 19:54
# @USER:     ShaJiu
# @Author  : shajiu
# @FileName: attention.py
# @Software: PyCharm
# @DATE:     2019/12/1 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import codecs
from pylab import mpl, text
"""针对源语言和目标语言画出Attention注意机制图像
   输入：注意机制权重矩阵
        源语言、目标语言
   输出：图像
"""
file = codecs.open("./corpus/attention.txt", "r", encoding="utf-8")
def read_attention():
    src = []
    tgt = []
    attentions = []
    count = 0
    for tmp in file:
        tmp=' '.join(tmp.split())
        tmp = tmp.split()
        if count==0:
            src=tmp
        else:
            tgt.append(tmp[0])
            attention=[]
            for tm in tmp[1:]:
                tm=tm.replace("*","")
                tm=float(tm)
                tm=round(tm,2)
                attention.append(tm)
            attentions.append(attention)
        count+=1

    attentions_np=np.array(attentions)
    attentions_np=attentions_np.reshape(len(tgt),len(src))  #行、列
    print("src:\n", src)
    print("attention\n",attentions_np)
    print("tgt:\n",tgt)
    return attentions_np,src, tgt

def seaborn_heatmap(attention, src, tgt):
    data = pd.DataFrame(attention, columns=src, index =tgt)
    cmap = sns.cubehelix_palette(start=1.5, rot=5, gamma=0.8, as_cmap=True, )
    ax = sns.heatmap(data.T, square=True, center=0)
    #ax = sns.heatmap(data.T,annot=True,square=True,center=0,, linewidths=0.05)
    ax.set_xlabel('target_sentence',fontdict={'family' : 'Times New Roman', 'size'   : 20})  #源语言
    ax.set_ylabel('source_sentence',fontdict={'family' : 'Times New Roman', 'size'   : 20})  #目标语言
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    #

    for item in ax.get_yticklabels():
        item.set_rotation(0)
        item.set_fontname('Times New Roman')

    for item in ax.get_xticklabels():
        item.set_rotation(90)
        item.set_fontname('Times New Roman')

    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 23,
             }

    """具体设置"""
    plt.rcParams["figure.figsize"]=(5.0,4.0)
    plt.title('Attention mechanism visualization(Fr-En)', y=1.05, fontdict={'family' : 'Times New Roman', 'size': 35})
    plt.rcParams['font.sans-serif'] = ['Times New Roman']

    #plt.subplots_adjust(top=0.8, bottom=0, right=1, left=0, hspace=0.2, wspace=0)
    plt.tick_params(labelsize=35)
    plt.xticks(rotation=45)

    plt.show()
    #plt.savefig('G:\ALC-2019\data\\result\opennmt\en-vi\\18-attention.source--.png', dpi=100)

if __name__ == '__main__':
    attentions, src, tgt=read_attention()
    seaborn_heatmap(attentions, src, tgt)