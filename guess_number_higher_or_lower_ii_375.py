# 蛮难理解的

http://www.cnblogs.com/grandyang/p/5677550.html
https://blog.csdn.net/fuxuemingzhu/article/details/82893656

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, L, R):
        if L >= R: return 0
        if dp[L][R]: return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
        return dp[L][R]

把递归改为迭代，方法如下：

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82893656
版权声明：本文为博主原创文章，转载请附上博文链接！
