
class Solution(object):
    def kthSmallest(self, matrix, k):
# https://zxi.mytechroad.com/blog/algorithms/binary-search/sp5-binary-search/
# binary search (kind of magic)


        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = l + (r - l) // 2
            total = 0
            for row in matrix:
                total += bisect.bisect_right(row, m)
            if total >= k:
                r = m
            else:
                l = m + 1
        return l

# max heap:
# http://www.cnblogs.com/grandyang/p/5727892.html

# min heap: 
# http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
        
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not visited[i+1][j]:
                visited[i+1][j] = True
                heapq.heappush(q, (matrix[i+1][j], i+1, j))
            if j + 1 < n and not visited[i][j+1]:
                visited[i][j+1] = True
                heapq.heappush(q, (matrix[i][j+1], i, j+1))
        return ans