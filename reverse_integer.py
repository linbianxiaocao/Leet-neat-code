"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? 
Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x < 0:
            sign = -1
        else:
            sign = 1
        x_str = str(abs(x))
        rx_str = x_str[::-1]
        rx = sign * int(rx_str)
        if rx > INT_MAX or rx < INT_MIN:
            return 0
        else:
            return rx