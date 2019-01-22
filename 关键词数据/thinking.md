* 文件是txt格式
* 文件前三行没用
* DE后面的某一篇文章的关键词
* ID：领域的关键词。有的文章有这个，有的没有
* ER PT *没用
* 关键词后用英文分号，最后一个没有对于这种，如果我想提取出关键词可以用正则表达式的方法，
   如“DE~~”。
* 由于某些文献本身的数量特别少，光用wos是不够的，需要使用百度中南和scopus作为辅助提取关键词。
* citespace需要在JAVA环境下安装，画出的图也不好看，我还是使用python networkx来做。
* 但是我要尽快，争取今天学明白，早点搞出第一张图，附带度中心性的表。
 
 
$ 正式代码思想如下：
* 先将DE后面的字符串匹配出来，并将这个字符串取出，
["Physical layer security;secrecy rate;potent"]

* 切开：['Physical layer security','secrecy rate','potent']
* 列表套列表

[
['Physical layer security','secrecy rate','potent'],
['Optimization',' resonant converter']
]

$ 网络图绘制
* 将Keywords中的小列表构成一个个列表，并设定weight=1。（'wireless power transfer','wireless',1）
* 重复添加已经存在的边时，要保证权重也相加。使用MultiGraph可以保证权重不丢失，然后再判断权重是否有多个，是则累积。
* 根据节点的度按从大到小排序，节点的度越大，节点的size越大。
%%++存在的问题数据梁仍然有些不足，70条数据太少，尽量让样本量大起来。