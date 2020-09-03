# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/205682/JavaC%2B%2BPython-BFS-Level-Order-Traversal
        
        
    # Also you may want to return earlier.
    # We can stop the first while loop when met the first null child.
    # From then on there should not be any more child.
    # This optimisation help reduce half of operations.
    
        if root is None:
            return True
        
        from collections import deque
        q = deque()
        q.append(root)
        while True:
            node = q.popleft()
            if node.left is None:
                if node.right is not None:
                    return False
                break
            q.append(node.left)
            if node.right is None:
                break
            q.append(node.right)
            
        while len(q) > 0:
            node = q.popleft()
            if node.left is not None or node.right is not None:
                return False
        
        return True        