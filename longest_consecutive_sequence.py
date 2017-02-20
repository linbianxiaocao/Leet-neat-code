"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

# We can use a HashSet to add and remove elements. HashSet is implemented by using a hash table. Elements are not ordered. The add, remove and contains methods have constant time complexity O(1).
# http://www.programcreek.com/2013/01/leetcode-longest-consecutive-sequence-java/
# http://blog.csdn.net/fightforyourdream/article/details/15024861


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        s = set()
        max_len = 1
        for e in nums:
            s.add(e)

        for e in nums:
            if e in s:
                left = e-1
                right = e+1
                count = 1
                s.remove(e)

                while left in s:
                    s.remove(left)
                    left -= 1
                    count += 1

                while right in s:
                    s.remove(right)
                    right += 1
                    count += 1

                max_len = max(max_len, count)

        return max_len
