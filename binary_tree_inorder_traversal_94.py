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


# CPP
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // Morris Traversal
    // https://www.cnblogs.com/grandyang/p/4297300.html
    // https://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        TreeNode *cur, *pre;
        cur = root;
        while (cur) {
            if (!cur->left) {
                res.push_back(cur->val);
                cur = cur->right;
            } else {
                pre = cur->left;
                while (pre->right && pre->right != cur) pre = pre->right;
                if (!pre->right) {
                    pre->right = cur;
                    cur = cur->left;
                } else {
                    pre->right = NULL;
                    res.push_back(cur->val);
                    cur = cur->right;
                }
            }
        }
        return res;
    }
};
