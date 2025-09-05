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

# Review binary search template
# https://zxi.mytechroad.com/blog/sp/sp5-binary-search/
# Leetcode 69. Sqrt(x)
# Leetcode 278. First Bad Version
# Leetcode 875. Koko Eating Bananas
# Leetcode 378. Kth Smallest Element in a Sorted Matrix

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

import bisect
import collections
from typing import List

# Leetcode 140. Word Break II
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
    
# Leetcode 140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    for prev in dp[j]:
                        dp[i].append((prev + " " + s[j:i]).strip())

        return dp[n]

# Leetcode 973. K Closest Points to Origin
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            heapq.heappush(h, (p[0]**2 + p[1]**2, p)) # min heap
        kPoints = []
        for i in range(k):
            p = heapq.heappop(h)[1]
            kPoints.append(p)
        return kPoints

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            heapq.heappush(h, (-p[0]**2-p[1]**2, p)) # simulate max heap
            if len(h) > k:
                heapq.heappop(h)
        
        kPoints = []
        while len(h) > 0:
            p = heapq.heappop(h)[1]
            kPoints.append(p)
        return kPoints

# Leetcode 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        
        # count frequency
        df = collections.defaultdict(int)
        for num in nums:
            df[num] += 1
        
        # 用最小堆，方便弹出最小的        
        for num, freq in df.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)
        
        while len(h) > 0:
            _, num = heapq.heappop(h)
            res.append(num)
        
        return res

# Leetcode 1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
# Leetcode 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses
    
# Leetcode 346. Moving Average from Data Stream
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)
    
# Leetcode 1014. Best Sightseeing Pair
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxLeft = values[0] + 0
        maxScore = 0
        for j in range(1, len(values)):
            maxScore = max(maxScore, maxLeft + values[j] - j)
            maxLeft = max(maxLeft, values[j] + j)
        return maxScore