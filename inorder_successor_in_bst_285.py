# https://www.jianshu.com/p/218f686d6494

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        successor = None
        while root != None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        # 原本的root = None 或者 p不存在与BST中，此刻root = None
        if root == None:
            return None

        # 找到p之后，如果p没有右儿子，则第一个比它大的数字就是刚刚记录的successor
        if root.right == None:
            return successor

        # 找到p之后，如果有右儿子，则找到右子树中的最左边的值（最小值）
        root = root.right
        while root.left != None:
            root = root.left

        return root


https://nb4799.neu.edu/wordpress/?p=2209
