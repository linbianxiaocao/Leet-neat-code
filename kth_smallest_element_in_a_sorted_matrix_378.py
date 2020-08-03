
class Solution(object):
    def kthSmallest(self, matrix, k):
# https://zxi.mytechroad.com/blog/algorithms/binary-search/sp5-binary-search/
# binary search (kind of magic)

# http://www.cnblogs.com/grandyang/p/5727892.html
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