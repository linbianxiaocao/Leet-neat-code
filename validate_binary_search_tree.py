# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inf = 10**10
        return self.validate(-inf, root, inf)

    def validate(self, min_val, root, max_val):
        if not root:
            return True
        if not min_val < root.val < max_val:
            return False
        return self.validate(min_val, root.left, root.val) and \
               self.validate(root.val, root.right, max_val)

