# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        mid_idx = len(nums) / 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root
