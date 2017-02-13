"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.lli = []
        self.li = []

        self.findSum(root, sum)

        return self.lli

    def findSum(self, root, sum):
        if root is None:
            return

        self.li.append(root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                self.lli.append(self.li)
        else:
            self.findSum(root.left, sum-root.val)
            self.findSum(root.right, sum-root.val)

        self.li = self.li[:-1]
        return
