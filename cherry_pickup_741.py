class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for k in range(1, 2*n-1):
            for i in range(n-1, -1, -1):
                for p in range(n-1, -1, -1):
                    j = k-i
                    q = k-p
                    if j<0 or j>=n or q<0 or q>=n or \
                    grid[i][j]<0 or grid[p][q]<0:
                        dp[i][p]=-1
                        continue
                    if i>0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p])
                    if p>0:
                        dp[i][p] = max(dp[i][p], dp[i][p-1])
                    if i>0 and p>0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p-1])
                    if dp[i][p] >=0:
                        if i != p:
                            dp[i][p] += grid[i][j] + grid[p][q]
                        else:
                            dp[i][p] += grid[i][j]

        return max(dp[n-1][n-1], 0)

http://www.cnblogs.com/grandyang/p/8215787.html
https://blog.csdn.net/luke2834/article/details/79365645
"最后就是t这一维我们可以通过滚动数组压掉，注意这样的话需要反向遍历更新dp"

note:
还要特别注意的是反向计算dp数组，这样的话可以复用一个二维的dp数组而不用针对一个新的k(步长和)就开辟一个新的二维数组。反向计算是为了保证能用到上一次(t-1)的dp数组的值去更新当前t的dp数组的值。如果正向计算，会把t-1的dp数组的值覆盖掉，导致错误的计算。
