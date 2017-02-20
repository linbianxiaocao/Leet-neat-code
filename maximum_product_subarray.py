"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
# I have thought out this solution too
# https://shenjie1993.gitbooks.io/leetcode-python/152%20Maximum%20Product%20Subarray.html
# http://www.cnblogs.com/zuoyuan/p/4019326.html


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_tmp, min_tmp = nums[0], nums[0]
        result = nums[0]

        for val in nums[1:]:
            a = val * max_tmp
            b = val * min_tmp
            c = val
            max_tmp = max(a, b, c)
            min_tmp = min(a, b, c)
            result = max(result, max_tmp)

        return result
