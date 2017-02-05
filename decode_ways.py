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

# http://bangbingsyb.blogspot.ca/2014/11/leetcode-decode-ways.html
# f[n] = f[n-1] (if '1'<=s[n]<='9') + f[n-2] (if s[n-1]s[n] is betwen 10 and 26)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]<'1' or s[0]>'9':
            return 0

        dp_l = [0]*(len(s)+1)
        dp_l[0] = 1
        dp_l[1] = 1

        for i in range(1, len(s)):
            v1 = 0
            v2 = 0
            if not s[i].isdigit():
                return 0
            if s[i] != '0':
                v1 = dp_l[i]
            v_two_digits = (ord(s[i-1])-ord('0'))*10 + (ord(s[i])-ord('0'))
            if v_two_digits >= 10 and v_two_digits <= 26:
                v2 = dp_l[i-1]
            dp_l[i+1] = v1 + v2
            if dp_l[i+1] == 0:
                return 0

        return dp_l[len(s)]


