# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
# http://www.cnblogs.com/zuoyuan/p/3722004.html
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)
        return res
        
    def preorder(self, root, level, res):
        if root:
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
            
class Solution2(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        nodes = [root]
        
        while nodes:
            res.append( [node.val for node in nodes] )
            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes

        return res
