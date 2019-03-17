# -*- coding: utf-8 -*-
# http://www.cnblogs.com/grandyang/p/5177285.html

"""
这道题还有一种O(n)的解法，根据题目要求的nums[0] <= nums[1] >= nums[2] <= nums[3]....，我们可以总结出如下规律：

当i为奇数时，nums[i] >= nums[i - 1]

当i为偶数时，nums[i] <= nums[i - 1]

那么我们只要对每个数字，根据其奇偶性，跟其对应的条件比较，如果不符合就和前面的数交换位置即可，参见代码如下：
"""
def wiggleSort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
            tmp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = tmp
    return nums

nums = [3, 5, 2, 1, 6, 4]
nums = [1, 6, 2, 5, 3, 4]
print(wiggleSort(nums))

# wiggle sort 2 http://www.cnblogs.com/grandyang/p/5139057.html
http://bookshadow.com/weblog/2015/12/31/leetcode-wiggle-sort-ii/
http://www.learn4master.com/interview-questions/leetcode/wiggle-sort-ii
https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing

my implementation:
重要点，find ingress point, which is based on mid but differs pending on whether length is even or odd
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        snums = sorted(nums)[::-1]
        mid = (len(nums)-1) / 2

        if len(nums) % 2 == 0:
            ingress = mid+1
        else:
            ingress = mid

        k = ingress
        for i in range(0, len(nums), 2):
            nums[i] = snums[k]
            k += 1

        k = 0
        for i in range(1, len(nums), 2):
            nums[i] = snums[k]
            k += 1


        return


