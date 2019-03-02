# python
# -*- coding:utf-8 -*-
# author liao_wk time
import json, os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MG = nx.MultiGraph()
plt.figure(figsize=(15, 15))
fileName = "Nuclear Reprogramming"
os.chdir("F:\\大道之君\\Breakingthrough-Techonologies-Data-Analysis\\关键词数据\\关键词Data\\"+fileName)
filename = fileName + '.json'
file = open(filename)
line_num = 0  # 设置初始行号为0
for line in file:
    if line_num == 0:
        line_num += 1
        Keywords = eval(line)  # 关键词列表的列表
        # keyword = ['wireless power transfer','wireless','Physical layer security']
        for keyword in Keywords:
            # edge_list=[['wireless power transfer','wireless',]）,\
            # ['wireless power transfer','Physical layer security',1]]
            edge_list = []
            # list(range(len(keyword)))=[0,...,len(keyword)-1]
            for word_num in list(range(len(keyword))):
                # word_number=[word_num+1,...,len(keyword)-1]
                for word_number in list(range(word_num+1, len(keyword))):
                    # word_edge = ['wireless power transfer','wireless',]
                    word_edge = list([keyword[word_num], keyword[word_number], 1])
                    edge_list.append(word_edge)
            MG.add_weighted_edges_from(edge_list)  # 每循环一次添加一个全连接的关键词网络
    elif line_num == 1:
        Keywords_freq = eval(line)
        break
file.close()
de = dict(MG.degree())  # MG节点度 de={'closed-loop control': 4}
de2 = [de[v]*2 for v in de.keys()]  # 节点的度构成的列表，节点的顺序不变。
#  labels_sort将de按值得大小从大到小排序得到元组组成的列表。
#  labels_sort=[（关键词,度）]
labels_sort = sorted(de.items(), key=lambda v: v[1], reverse=True)
labels_word = labels_sort[0:10]  # 取前10个关键词
dd = {}  # dd={关键词：关键词}
for label_word in labels_word:
    dd[label_word[0]] = label_word[0]
# pos设置图的框架
pos = nx.spring_layout(MG)
# 只标记记前10个关键词
nx.draw_networkx_labels(MG, pos, labels=dd, font_size=15)
# 按度的大小标记节点的大小
nx.draw_networkx(MG, pos, with_labels=False, font_size=12, node_size=de2)

#  储存MultiGraph的度
with open(filename, 'a') as f_obj:
    f_obj.write('\n')
    json.dump(labels_sort, f_obj)

#  横向合并Keywords_freq和labels_sort列表，导入到csv文档中，输出前10行。
df1 = pd.DataFrame(np.array(Keywords_freq), columns=["Keyword_1", "frequency"])
df2 = pd.DataFrame(np.array(labels_sort), columns=["Keyword_2", "degreee"])
df = pd.concat([df1, df2], axis=1)
print(df.loc[0:6])

# 导入到csv文件中
df.to_csv(fileName+"_Keywords.csv")
# 输出网络图
plt.savefig(fileName+'.jpg')
plt.savefig(fileName+'.pdf')
plt.show()
