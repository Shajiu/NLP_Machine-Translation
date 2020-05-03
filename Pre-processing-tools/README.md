## 本仓库存储NMT中预处理时所使用的一些工具。
### 1.[index_word.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/index_word.py)将编号写入的句子转换为词语。
### 2.[Merge_parallel_corpus.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/Merge_parallel_corpus.py)将把平行语料写入到一个文件中格式为如下：
##### “Source:眼里怎会有泪水。Target:ཁྲ་ཆུང་མིག་ལ་མཆི་མ་མེད།”。
### 3.[mteval-txt-xml.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/mteval-txt-xml.py)处理测试数据:将正规的数据转化为标准的测试数据--为CWMT2018测试工具准备数据
##### 输入:数据测试集文件  输出:标准的XMl格式数据   源文:srcset   参考:refset   译文:tstset
