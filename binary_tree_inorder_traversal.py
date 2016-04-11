# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        li = []
        self.recursive_inorder(root, li)
        return li
        
    def recursive_inorder(self, root, li):
        if root:
            self.recursive_inorder(root.left, li)
            li.append(root.val)
            self.recursive_inorder(root.right, li)


class Solution2(object):
    # http://www.cnblogs.com/zuoyuan/p/3720273.html
    # http://www.gocalf.com/blog/traversing-binary-tree.html
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        li = []
        st = []

        while root or st:
            if root:
                st.append(root)
                root = root.left
            else:
                root = st.pop()
                li.append(root.val)
                root = root.right

        return li
