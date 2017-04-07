# Given a sorted array consisting of only integers where every element appears
# twice except for one element which appears once. Find this single element
# that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution(object):
    # O(N) solution
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for num in nums:
            r = r ^ num
        return r

    # O(log n) solution
    # http://bookshadow.com/weblog/2017/03/11/leetcode-single-element-in-a-sorted-array/
    def singleNonDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = (lo + hi) >> 1
            if nums[mi] == nums[mi-1]:
                if (mi - lo - 1) & 1:
                    hi = mi - 2
                else:
                    lo = mi + 1
            elif nums[mi] == nums[mi+1]:
                if (mi - lo) & 1:
                    hi = mi - 1
                else:
                    lo = mi + 2
            else:
                return nums[mi]

        return nums[lo]
