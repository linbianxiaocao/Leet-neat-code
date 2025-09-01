# Review binary search template
# https://zxi.mytechroad.com/blog/sp/sp5-binary-search/
# Leetcode 69. Sqrt(x)
# Leetcode 278. First Bad Version
# Leetcode 875. Koko Eating Bananas
# Leetcode 378. Kth Smallest Element in a Sorted Matrix

# Leetcode 199. Binary Tree Right Side View
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self._rightSideView(root, 0, result)
        return result

    def _rightSideView(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append(node.val)
        self._rightSideView(node.right, level + 1, result)
        self._rightSideView(node.left, level + 1, result)

# Leetcode 1249. Minimum Remove to Make Valid Parentheses
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        to_remove = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove = to_remove.union(set(stack))
        return ''.join(char for i, char in enumerate(s) if i not in to_remove)

# Leetcode 339. Nested List Weight Sum
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger], depth=1) -> int:
        total = 0
        for elem in nestedList:
            if elem.isInteger():
                total += elem.getInteger() * depth
            else:
                total += self.depthSum(elem.getList(), depth + 1)
        return total
        
# Leetcode 220. Contains Duplicate III
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Solve with sorted solution
        if k <= 0 or t < 0:
            return False

        sorted_nums = []
        for i, num in enumerate(nums):
            if i > k:
                sorted_nums.remove(nums[i - k - 1])
            pos = bisect.bisect_left(sorted_nums, num - t)
            if pos < len(sorted_nums) and abs(sorted_nums[pos] - num) <= t:
                return True
            bisect.insort(sorted_nums, num)
        return False
        
# Leetcode 1254. Number of Closed Islands (Compare with Leetcode 200. Number of Islands)
class Solution(object):
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # fill land (0) connected to border with water (1) through dfs
        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0 or j == 0 or i == self.rows - 1 or j == self.cols - 1:
                    if grid[i][j] == 0:
                        self.dfs(grid, i, j)
        res = 0
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):      
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or grid[i][j] == 1:
            return
        grid[i][j] = 1
        for dir in self.dirs:
            ni, nj = i + dir[0], j + dir[1]
            self.dfs(grid, ni, nj)

# Leetcode 305. Number of Islands II
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                return 1
            return 0

        parent = {}
        count = 0
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r, c in positions:
            if (r, c) in parent:
                result.append(count)
                continue
              
            parent[(r, c)] = (r, c)
            count += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:
                    count -= union((r, c), (nr, nc))
            result.append(count)
        return result
