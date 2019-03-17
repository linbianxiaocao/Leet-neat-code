# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 双层递归
# reference: http://bookshadow.com/weblog/2016/10/23/leetcode-path-sum-iii/
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        ans = self.traverse(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans

    def traverse(self, root, val):
        if not root: return 0
        res = (val == root.val)
        res += self.traverse(root.left, val - root.val)
        res += self.traverse(root.right, val - root.val)
        return res
