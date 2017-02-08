"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

Hint:
Use two dictionaries
"ab", "bb" -> False
"a", "b" -> True
A bit tricky. I spent more than an hour getting it right. 

Idea is actually very simple:
    d1 records the mapping of c1 to c2
    d2 records the inverse, in another word, c2 is mapped from c1
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if d1.get(s[i]) is None and d2.get(t[i]) is None:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            else:
                if d1.get(s[i]) != t[i] or d2.get(t[i]) != s[i]:
                    return False
        return True
