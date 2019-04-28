# http://www.cnblogs.com/grandyang/p/5185561.html, https://www.cnblogs.com/grandyang/p/5351347.html

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        left = 0
        m = collections.defaultdict(int)
        for i in range(len(s)):
            m[s[i]] += 1
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
