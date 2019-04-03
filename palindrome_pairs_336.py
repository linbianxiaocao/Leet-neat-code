https://blog.csdn.net/fuxuemingzhu/article/details/83616356

利用字典wmap保存单词 -> 下标的键值对

遍历单词列表words，记当前单词为word，下标为idx：

1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案

     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/83616356
版权声明：本文为博主原创文章，转载请附上博文链接！

note: 理解思路后就不难了，关键在于建立一个字典，然后对每个单词分情况讨论
