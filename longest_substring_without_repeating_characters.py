"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters 
for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {}
        max_len = 0
        head = 0
        tail = -1
        for (i, v) in enumerate(s):
            if v not in d:
                d[v] = i
                tail = i
            else:
                if d[v] >= head:
                    max_len = max(tail - head + 1, max_len)
                    head = d[v] + 1
                    tail = i
                    d[v] = i
                else:
                    d[v] = i
                    tail = i
            
        return max(tail - head + 1, max_len)        