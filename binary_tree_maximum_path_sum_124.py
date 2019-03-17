# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# reference:https://blog.csdn.net/qqxx6661/article/details/78484940,https://shenjie1993.gitbooks.io/leetcode-python/124%20Binary%20Tree%20Maximum%20Path%20Sum.html
# my own implementation
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -float('inf')

        self.dfs(root)

        return self.maxSum

    def dfs(self, root):
        if root is None:
            return 0

        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        curMax = root.val
        if leftMax > 0:
            curMax += leftMax
        if rightMax > 0:
            curMax += rightMax

        self.maxSum = max(self.maxSum, curMax)

        return max(root.val, root.val+leftMax, root.val+rightMax)
