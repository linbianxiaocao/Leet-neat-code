# https://www.cnblogs.com/grandyang/p/4290148.html

1. 递归解法比较难理解
2. 层序遍历容易理解
3. 解法三O(1)空间要想想，是可以理解的, 要从框架结构上理解，关键是两个节点，一个root，一个dummy，不停的更新, 同样的解法这里写的比较好看http://rainykat.blogspot.com/2017/02/leetcodef-117-populating-next-right.html

# 比较i http://www.cnblogs.com/grandyang/p/4288151.html
我们再来看下面这种碉堡了的方法。用两个指针start和cur，其中start标记每一层的起始节点，cur用来遍历该层的节点，设计思路之巧妙，不得不服啊
