https://www.cnblogs.com/ZhaoxiCheung/p/LeetCode-SumofDistancesinTree.html
https://blog.csdn.net/qq_41445952/article/details/80977067

每个节点保存两个值，一个是其子树的节点个数（包括自身节点也要计数）nodesum[ ]，一个是其子树各点到它的距离 dp[ ]

sum 表示 以这个节点为根的子树的所有子节点到该节点的距离的和；

两个递归
