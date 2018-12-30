# https://leetcode.com/problems/add-two-numbers-ii/
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# 简单题，稍微想想，和i相比，链表的顺序反过来怎么处理
method 1. sum each place first, store a separate index array for the carry, and process carries at 2nd run
