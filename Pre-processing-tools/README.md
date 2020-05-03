## 本仓库存储NMT中预处理时所使用的一些工具。
### 1.[index_word.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/index_word.py)将编号写入的句子转换为词语。
### 2.[Merge_parallel_corpus.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/Merge_parallel_corpus.py)将把平行语料写入到一个文件中格式为如下：
##### “Source:眼里怎会有泪水。Target:ཁྲ་ཆུང་མིག་ལ་མཆི་མ་མེད།”。
### 3.[mteval-txt-xml.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/mteval-txt-xml.py)将正规的数据转化为标准的测试数据--为CWMT2018测试工具准备数据
##### 输入:数据测试集文件  输出:标准的XMl格式数据   源文:srcset   参考:refset   译文:tstset
### 4.[parallel_corpus_clean.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/parallel_corpus_clean.py)输入分词后的文本     读取文件必须放在项目的根目录下、过滤特征有： 1.双语句子长度比率 2.重复句子。
### 5.[Regular_removal_xml.py:](https://github.com/Shajiu/NLP_Machine-Translation/blob/master/Pre-processing-tools/Regular_removal_xml.py)正则表达---通过匹配提取文本内容-----从标准的测试数据集中可以删除xml格式提取正文内容、去除文本开头空格、去除文本末尾空格、从xml文本中提取内容写入到txt中整理。
