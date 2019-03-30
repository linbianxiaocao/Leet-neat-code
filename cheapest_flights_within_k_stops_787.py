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

这样写更清楚简洁：
        dp = [float('inf')] * n
        dp[src] = 0
        for i in range(K+1):
            tempDp = dp[:]
            for flight in flights:
                dp[flight[1]] = min(tempDp[flight[0]] + flight[2], dp[flight[1]])
        return dp[dst] if dp[dst] < float('inf') else -1

or DFS/BFS: https://blog.csdn.net/fuxuemingzhu/article/details/83307822
huahua: https://www.youtube.com/watch?v=PLY-lbcxEjg

DFS:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        visited = [0] * n
        ans = [float('inf')]
        self.dfs(graph, src, dst, K + 1, 0, visited, ans)
        return -1 if ans[0] == float('inf') else ans[0]

    def dfs(self, graph, src, dst, k, cost, visited, ans):
        if src == dst:
            ans[0] = cost
            return
        if k == 0:
            return
        for v, e in graph[src].items():
            if visited[v]: continue
            if cost + e > ans[0]: continue
            visited[v] = 1
            self.dfs(graph, v, dst, k - 1, cost + e, visited, ans)
            visited[v] = 0

BFS:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        ans = float('inf')
        que = collections.deque()
        que.append((src, 0))
        step = 0
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    que.append((v, cost + w))
            if step > K: break
            step += 1
        return -1 if ans == float('inf') else ans


dijikstra (failed):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e

        unVisited = set(i for i in range(n))
        distances = [float('inf')] * n
        distances[src] = 0

        step = 0
        while step <= K:
            currNode = min(unVisited, key=lambda x:distances[x])
            for v, w in graph[currNode].items():
                if v in unVisited:
                    distances[v] = min(distances[v], distances[currNode]+w)
            unVisited.remove(currNode)
            step += 1
        return -1 if distances[dst] == float('inf') else distances[dst]
