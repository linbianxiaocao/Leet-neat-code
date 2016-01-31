# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


# Analysis:
# Key point is to save the previous result, e.g. ()(), when the second ( is scanned, the result length should add the first pair of ().
# 
# Some special cases should be considered:
# ()()  max = 4
# )()() max = 4
# (()() max = 4
# ()(() max = 2
# 
# If current character is '(', push into the stack.
# If current character is ')',
#     Case 1:  the stack is empty, reset previous result to zero. Here we renew a pointer to store the earliest index.
#     Case 2: the stack is not empty, pop the top element. if the top element is '(' , (which means a () pair is found), then if the poped stack is empty, (which means the previous pairs should be added.), len = current pos - previous pos +1; If the poped stack is not empty, len = current pos- index of stack top element.
 
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxLen = 0
        for i in range(len(s)):
            topIndex = stack[-1]
            if s[i] == ')' and topIndex != -1 and s[topIndex] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1])
            else:
                stack.append(i)
        return maxLen
