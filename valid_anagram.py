"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""

# O(n log n) time
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        
# O(n) time        
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}
        for ls in s:
            if ls in d:
                d[ls] += 1
            else:
                d[ls] = 1
        
        for lt in t:        
            if lt in d:
                d[lt] -= 1
            else:
                return False
                
        if all([val == 0 for val in d.values()]):
            return True
        else:
            return False
            
# O(n) time        
class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}
        for (ls, lt) in zip(s, t):
            if ls in d:
                d[ls] += 1
            else:
                d[ls] = 1
        
            if lt in d:
                d[lt] -= 1
            else:
                d[lt] = -1
                
        if all([val == 0 for val in d.values()]):
            return True
        else:
            return False

# O(n) time        
class Solution4(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}
        for ls in s:
            if ls in d:
                d[ls] += 1
            else:
                d[ls] = 1
        
        for lt in t:
            if lt not in d:
                return False
            d[lt] -= 1
            if d[lt] < 0:
                return False
        
        return True