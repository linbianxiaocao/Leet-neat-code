方法1：
递归把嵌套列表摆平，值存入一个queue或者list
https://blog.csdn.net/fuxuemingzhu/article/details/79529982

这个题很简单，一遍就过了，不懂为什么是中等难度。

需要我们设计一个数据结构保存嵌套数组的每个元素，一般选择列表，但为了速度快，我们选择了队列。

重点是利用递归把整个嵌套的列表迭代器给压平。注意，题目已经给了我们它的数据结构，而不是普通的list。所以我们必须用他的函数。题目中虽然是多重嵌套，但是归根到底，对于每层的嵌套都是一个一维数组而已。因此，不要想复杂，直接循环该一维数组，如果是整数，添加到队列中，如果是嵌套的列表则继续解嵌套。。最后的结果是有按照从左到右有序的，这个可以放心哈～～

方法2：不直接把嵌套列表摆平，而是在每次调用hasNext()方法时维护一个数据结构
http://www.cnblogs.com/grandyang/p/5358793.html
a) 用栈，注意需要从后往前压栈
b) 用队列，注意插入队列时要插在前面，这个和平时队列的用法有点不同


