http://www.cnblogs.com/grandyang/p/5297683.html
https://www.jianshu.com/p/c38f93f6431f

# my python
i# 这里用一个小trick，我们第一遍历的时候，都是找0的位置，遍历完后，我们将其赋为-1，这样下一轮遍历我们就找-1的位置，然后将其都赋为-2，
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        val = 0
        sum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # BFS
                    q = collections.deque()
                    q.append((i, j))
                    dist = [[0] * n for _ in range(m)]
                    while len(q):
                        (a, b) = q.popleft()
                        for dir in dirs:
                            x, y = a + dir[0], b + dir[1]
                            if x >= 0 and x < m and y >= 0 and y < n and \
                                grid[x][y] == val:
                                grid[x][y] -= 1
                                dist[x][y] = dist[a][b]+1
                                sum[x][y] += dist[x][y]
                                q.append((x, y))
                    val -= 1

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == val:
                    res = min(sum[i][j], res)

        return -1 if res == float('inf') else res
