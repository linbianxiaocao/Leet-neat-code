class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        base = 1
        while x / base >= 10:
            base *= 10
        while x > 0:
            if x / base != x % 10:
                return False
            x = x % base /10
            base /= 100
        return True