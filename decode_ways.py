# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# 
# The number of ways decoding "12" is 2.

# http://yucoding.blogspot.ca/2013/01/leetcode-question-26-decode-ways.html
# incomplete
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        lres = []
        if s[0] != 0:
            lres.append(1)
        else:
            lres.append(0)

        if len(s) == 1:
            return lres[0]

        if self.valid(s[0:2]):
            lres.append(1)
        

    def valid(self, s):
        if len(s) == 0:
            return False
        if s[0] == '0':
            return False

