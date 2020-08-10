# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/565677/Python-Using-Dictionary-Beats-98        
        dic = defaultdict(list)
        self.helper(0, 0, root, dic)
        result = []
        for i in sorted(dic.keys()):
            result.append( [j[1] for j in sorted(dic[i])] )
        return result
        
    
    def helper(self, placement, level, root, dic):
        if not root:
            return
        dic[placement].append((level, root.val)) # first is level, for sorting  
        self.helper(placement-1, level+1, root.left, dic)
        self.helper(placement+1, level+1, root.right, dic)