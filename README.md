# NLP_Machine-Translation
### 本仓库存储了一些基本的NMT相关的项目的公开代码
### 一、[BPE:](https://github.com/Shajiu/NLP_Machine-Translation/tree/master/BPE)将把BPE原始码很好的简化和浓缩，可便于入门者理解和使用。
### 二、[Attention_visualization](https://github.com/Shajiu/NLP_Machine-Translation/tree/master/Attention_visualization)对译文质量进行Attention可视化以及BLEU值的折线图。
##### 1.[corpus/attention.txt:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/corpus/attention.txt)为源文跟译文对应词之间的Attention矩阵值，其中横坐标表示Source，纵坐标表示Target。
##### 2.[attention.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/attention.py)针对源语言和目标语言画出Attention注意机制图像。![](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/Fr-En.jpg)
##### 3.[sentence-attention.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/sentence-attention.py)针对源语言和目标语言画出Attention注意机制图像。![Attention](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/sns_heatmap_normal.jpg)
##### 4.[test_bleu.py](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/test_bleu.py)针对三个不同测试集上的BLEU值值的折线图![](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Attention_visualization/easyplot.jpg)
