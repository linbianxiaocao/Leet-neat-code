# my own solution, tle

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.pathSum = float('inf')
        self.dfs(0, 0, [], triangle)
        return self.pathSum


    def dfs(self, level, index, path, triangle):
        if level == len(triangle):
            self.pathSum = min(self.pathSum, sum(path))
            return

        # 这样不work: path += [triangle[level][index]]
        self.dfs(level+1, index, path + [triangle[level][index]], triangle)
        self.dfs(level+1, index+1, path + [triangle[level][index]], triangle)

        return

# dp: https://shenjie1993.gitbooks.io/leetcode-python/120%20Triangle.html
https://blog.csdn.net/aliceyangxi1987/article/details/52225849

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
