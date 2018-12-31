
# i
# 并查集的方法
# 我刚开始想到的是深度优先搜索，如果碰到两个节点都visited过了，就返回

Class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge


    def findRoot(self, x, tree):
        if tree[x] == -1: return x
        else:
            root = self.findRoot(tree[x], tree)
            tree[x] = root
            return root
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80487064
版权声明：本文为博主原创文章，转载请附上博文链接！

I like this UFS method better (that does not initialize to -1, but to the same number as index
解题思路：
解法I 并查集（Union Find Set）

Python代码：
http://bookshadow.com/weblog/2017/09/24/leetcode-redundant-connection/
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = list(range(max(reduce(operator.add, edges)) + 1))
        def find(a):
            while p[a] != a: a = p[a]
            return a
        for s, t in edges:
            ps, pt = find(s), find(t)
            if ps == pt: return [s, t]
            p[ps] = pt

http://www.cnblogs.com/grandyang/p/7628977.html?spm=a2c4e.11153940.blogcont327209.8.7adc3847qJg52W




# skipped ii since it's more complicated and takes more time to understand
