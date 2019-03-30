https://www.cnblogs.com/grandyang/p/6944331.html

所以这里博主就不创建自定义类了，而是使用两个哈希表来做，其中dirs建立了路径和其对应的包含所有文件和文件夹的集合之间的映射，files建立了文件的路径跟其内容之间的映射。

最开始时将根目录"/"放入dirs中，然后看ls的实现方法，如果该路径存在于files中，说明最后一个字符串是文件，那么我们将文件名取出来返回即可，如果不存在，说明最后一个字符串是文件夹，那么我们到dirs中取出该文件夹内所有的东西返回即可。

https://blog.csdn.net/magicbean2/article/details/78950619
文件系统构成了一个树状结构，所以本题目的一个解法就是建立一个树状结构来模拟文件系统。但是由于本题目是简化版的文件系统，所以我们也可以用更简单的字典树来实现。我们定义一个TrieNode的结构来统一表示文件和文件夹。如果isFile为true，则content表示文件的具体内容，此时children无效；否则children表示文件夹下的子文件（夹）列表，而content无效。下面给出各个函数的实现说明：
---------------------
作者：魔豆Magicbean
来源：CSDN
原文：https://blog.csdn.net/magicbean2/article/details/78950619
版权声明：本文为博主原创文章，转载请附上博文链接！
