"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:
(-1, 0, 1)
(-1, -1, 2)

REF: https://en.wikipedia.org/wiki/3SUM
Quadratic algorithm
Suppose the input array is S[0..n-1]. 3SUM can be solved in O(n^2) time on average by inserting each number S[i] into a hash table, and then for each index i and j, checking whether the hash table contains the integer -(S[i]+S[j]).

Alternatively, the algorithm below first sorts the input array and then tests all possible pairs in a careful order that avoids the need to binary search for the pairs in the sorted list, achieving worst-case O(n^2) time, as follows.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # (a) this avoids finding duplicate triplets
            j = i + 1
            k = len(nums) - 1
            while j < k:           
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum < 0:
                    j += 1
                elif temp_sum > 0:
                    k -= 1
                else:  # found a triplet of sum 0
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in triplets: # (b) this avoids finding duplicate triplets
                        triplets.append(triplet)
                    j += 1
                    k -= 1
        
        return triplets
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        