"""
Given an array of integers, find two numbers such that they add up to a specific target number.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
            
        d = {}    
        for (i, val) in enumerate(nums):
            expect = target - val
            if expect in d:
                return [d[expect] + 1, i + 1]
            if val not in d:
                d[val] = i
            
        return []
            