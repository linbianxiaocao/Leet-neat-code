# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:16:24 2015

@author: jieyan
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows <= 1:
            return s
        lens = len(s)    
        period = 2 * (numRows - 1)
        rstr = ""
        
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                start = i                
                while start <= lens - 1:
                    rstr += s[start]
                    start += period
            else:                
                start1 = i
                start2 = period - i
                while start1 <= lens - 1 and start2 <= lens - 1:
                    rstr = rstr + s[start1] + s[start2]
                    start1 += period
                    start2 += period
                if start1 <= lens - 1:
                    rstr += s[start1]
        
        return rstr             
                    
                