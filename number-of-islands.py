# https://blog.csdn.net/fuxuemingzhu/article/details/81126995


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        for dir in self.dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)
