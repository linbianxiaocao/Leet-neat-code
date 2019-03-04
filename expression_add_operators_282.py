# http://bookshadow.com/weblog/2015/09/16/leetcode-expression-add-operators/

DFS（深度优先搜索）

将字符串拆解成left + operator + right的形式，针对left执行递归

注意：包含前导0的运算数是无效的。

例如，通过"00+9"获得目标值9是不正确的。


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def isLeadingZeros(num):
            return num.startswith('00') or int(num) and num.startswith('0')
        def solve(num, target, mulExpr = '', mulVal = 1):
            ans = []
            #remove leading zeros
            if isLeadingZeros(num):
                pass
            elif int(num) * mulVal == target:
                ans += num + mulExpr,
            for x in range(len(num) - 1):
                lnum, rnum = num[:x+1], num[x+1:]
                #remove leading zeros
                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                #op = '+'
                for left in solve(lnum, target - rightVal):
                    ans += left + '+' + right,
                #op = '-'
                for left in solve(lnum, target + rightVal):
                    ans += left + '-' + right,
                #op = '*'
                for left in solve(lnum, target, '*' + right, rightVal):
                    ans += left,
            return ans
        if not num:
            return []
        return solve(num, target)

