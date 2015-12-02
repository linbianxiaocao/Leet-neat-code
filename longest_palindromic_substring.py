# -*- coding: utf-8 -*-
"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
"""

class Solution(object):
    def expandAroundCenter(self, s, c1, c2):
        l = c1
        r = c2        
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
            
        longest_p = s[0]
        for i in range(len(s)):
            s1 = self.expandAroundCenter(s, i, i)
            if len(s1) > len(longest_p):
                longest_p = s1
            s2 = self.expandAroundCenter(s, i, i+1)
            if len(s2) > len(longest_p):
                longest_p = s2
                
        return longest_p
            