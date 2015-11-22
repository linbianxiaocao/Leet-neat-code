"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p2] == nums[p1]:
                continue
            p1 += 1
            if nums[p1] != nums[p2]:
                nums[p1] = nums[p2]

        return p1 + 1