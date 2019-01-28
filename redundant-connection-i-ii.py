
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



ii
http://www.cnblogs.com/grandyang/p/8445733.html
没有全部明白，但是大概思路能跟上，记住要分三种情况
class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> root(n + 1, 0), first, second;
        for (auto& edge : edges) {
            if (root[edge[1]] == 0) {
                root[edge[1]] = edge[0];
            } else {
                first = {root[edge[1]], edge[1]};
                second = edge;
                edge[1] = 0;
            }
        }
        for (int i = 0; i <= n; ++i) root[i] = i;
        for (auto& edge : edges) {
            if (edge[1] == 0) continue;
            int x = getRoot(root, edge[0]), y = getRoot(root, edge[1]);
            if (x == y) return first.empty() ? edge : first;
            root[x] = y;
        }
        return second;
    }
    int getRoot(vector<int>& root, int i) {
        return i == root[i] ? i : getRoot(root, root[i]);
    }
};
