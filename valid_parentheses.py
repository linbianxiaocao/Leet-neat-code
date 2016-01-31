# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        pm = {')':'(', ']':'[', '}':'{'}
        for e in s:
            if e in ('(', '[', '{'):
                st.append(e)
            elif e in (')', ']', '}'):
                if st == [] or st.pop() != pm[e]:
                    return False
        
        if st == []:
            return True
        else:
            return False

