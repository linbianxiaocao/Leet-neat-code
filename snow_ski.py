OA是12，题目是Round Prices那道题，做完之后HR马上约了几天后有一个15分钟的电话follow up，follow up的内容就是简单让我重复一下我的思路和做法，没有问follow up questoin.

电面是一位超级好的国人大哥，题目是Combination Sum的那道题，要求是用最少的元素组成target，比如给一个输入 [1, 2, 3, 4, 5]， target = 9. 组合方式可以是 2+2+2+2+1, 3+3+3, 4+5，最少的话就是4+5只需要两个数字，返回2就行。可以用搜索做，可以用无限背包DP做。用DP做的，但是写的不是很流畅，非常nice的国人大哥也给了提示。

Onsite 2轮cross functional + 2轮coding + 1轮system design + 1轮dive deep简历

第1 & 2 轮 ： Cross functional就是纯聊天面，问到的问题有：

      - 为什么要来Airbnb
      - 过期的经历里你有什么经历是感觉特别自豪的（为社会做过啥贡献）
      - 有没有给人什么feedback，主要侧重于不同意见的feedback（应该是考察意见不同的时候怎么处理）

第3轮 Coding 国人小哥

      - 问题是滑雪问题，本质是一个有向图的问题，包装了一层滑雪的外壳。
     - 背景是一个滑雪选手从高山上往下滑，会遇到不同的checkpoint，每一个checkpoint有自己的point，然后每个edge有distance。经过每一个checkpoint所得到的score是通过一个包含point和distance的式子算出来的（比如2 * point + distance之类的）。最终求从最高点往下滑能得到的最大score是多少，用BFS就可以。
     - 类似下图，从A出发，最终可以到 I 或者 J，求到 I 或者 J 能得到的最大score是多少。

第4轮 Coding 国人new grad小哥 + 外国妹shadow

     - 问题是Sliding Puzzle那道题。board的表示要自己定义，然后要自己写怎么shuffle board，然后输出boolean值表示是否可以恢复到需要的样子。

第5轮 System Design 国人大哥

     - 设计RSS Feeder，主要是focus在数据库的设计。User表，Provider表，News Feed表之类的。
     - 其中问了一些周边问题，比如说User表的password怎么存，如果数据库被脱裤了，hacker有可能会用rainbow table attack把常用的密码的hash值反向解析出来，怎么预防这种情况。应该回答Salted Password Hashing，把用户的password加盐然后再hash存起来。
     - 另外一个问题是User看过的news feeds就不再展示，怎么实现。
     - Pull model怎么快速取某个用户的news feeds。我提出的是取回来，本地merge。然后国人大哥居然说用IN语句，select * from news_feed_table where provider_id IN (select provider_id from user_provider_table where user_id = 5) orderby created_at limit 100; 我说本地可能会更快，九章令狐冲老师明明说In并不能加快Sql查询啊。但是大哥说在数据库端用in并且排序会更快。

第6轮 Dive Deep  Manager

     - BQ一堆：最challenging的经历，工作中学到什么，有不同意见怎么处理. check 1point3acres for more.
     - 然后就是自己选一个project说说架构，怎么设计的，有什么trade off等等。



滑雪这个题bfs会被迫重复走很多path，可以按照topo排序来做就行了到达 O（E+V）
嗯，这题如果没有环（按理来说应该没有，有的话就可以无限走环），可以拓扑排序，维护一个scores列表，拓扑排序的时候更新max_score。最后读取scores[dst]，
附伤python解法和一组测试样例。如果有错误望请指正。


图的最长路径问题：
https://blog.csdn.net/sunmenggmail/article/details/7739390
1。
肯定不能用dijkstra算法，这是因为，Dijkstra算法的大致思想是每次选择距离源点最近的结点加入，然后更新其它结点到源点的距离，直到所有点都被加入为止。当每次选择最短的路改为每次选择最长路的时候，出现了一个问题，那就是不能保证现在加入的结点以后是否会被更新而使得到源点的距离变得更长，而这个点一旦被选中将不再会被更新。例如这次加入结点u，最长路为10，下次有可能加入一个结点v，使得u通过v到源点的距离大于10，但由于u在之前已经被加入到集合中，无法再更新，导致结果是不正确的。

     如果取反用dijkstra求最短路径呢，记住，dijkstra不能计算有负边的情况。。。

2.
可以用   Bellman-Ford   算法求最长路径，只要把图中的边权改为原来的相反数即可。也可以用Floyd-Warshall   算法求每对节点之间的最长路经，因为最长路径也满足最优子结构性质，而Floyd算法的实质就是动态规划。但是，如果图中含有回路，Floyd算法并不能判断出其中含有回路，且会求出一个错误的解；而Bellman-Ford算法则可以判断出图中是否含有回路。

3. 如果是有向无环图，先拓扑排序，再用动态规划求解。
---------------------
作者：sunmenggmail
来源：CSDN
原文：https://blog.csdn.net/sunmenggmail/article/details/7739390
版权声明：本文为博主原创文章，转载请附上博文链接！

- 另外一道滑雪题
https://segmentfault.com/a/1190000003890737
给出一个矩阵，求矩阵中从某个点开始，最长的下降路径。路径可以走上下左右四个方向。求最长路径的长度。

1 2 3 4
5 6 7 8
其中一条最长路径是8 7 6 5 1

note: 理清思路了后应该不难，摆好dfs的框架，自己用Pyton实现一遍


