# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self._rightSideView(root, 0, result)
        return result

    def _rightSideView(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append(node.val)
        self._rightSideView(node.right, level+1, result)
        self._rightSideView(node.left, level+1, result)
