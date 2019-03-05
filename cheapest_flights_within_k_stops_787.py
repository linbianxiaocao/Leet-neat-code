https://blog.csdn.net/magicbean2/article/details/79742529
修改Bellman-Ford算法,https://www.youtube.com/watch?v=2raV0H9KqY8

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dp = [float('inf')] * n
        dp[src] = 0
        for i in range(K+1):
            tempDp = dp[:] // 注意这里使用一个tempDp数组，为了每次循环使用前一次的数值，满足K stop的要求
            for flight in flights:
                tempDp[flight[1]] = min(dp[flight[0]] + flight[2], tempDp[flight[1]])
            dp = tempDp
        return dp[dst] if dp[dst] < float('inf') else -1

or BFS: https://blog.csdn.net/fuxuemingzhu/article/details/83307822
