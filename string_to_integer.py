"""
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        newStr = []
        for i in range(len(str)):
            if '0' <= str[i] <= '9' or (str[i] in ('+', '-') and i == 0):
                newStr.append(str[i])
            else:
                break
        if newStr in ([], ['+'], ['-']):
            return 0
        
        ri = int(''.join(newStr))
        if -2147483648 <= ri <= 2147483647:
            return ri
        elif ri > 2147483647:
            return 2147483647
        else:
            return -2147483648
            
class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign*sum
        
class Solution3:  
    def atoi(self, str):
        
        INT_MAX, INT_MIN = 2147483647, -2147483648
        
        if len(str) == 0:
            return 0
                
        str = str.strip()
        index = 0
        sign = 1
        
        if str[index] == '-':
            sign = -1
        if str[index] in "-+":
            index += 1
                
        result = 0
        while index < len(str) and str[index].isdigit():
            result = result * 10 + (ord(str[index]) - ord('0'))
            index += 1
                        
        result *= sign
        
        if sign == 1 and result >= INT_MAX:
            return INT_MAX
        elif sign == -1 and result <= INT_MIN:
            return INT_MIN
                
        return result