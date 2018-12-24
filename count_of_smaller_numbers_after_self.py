"""
You are given an integer array nums and you have to return a new
counts array. The counts array has the property where counts[i]
is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left jumps.
#https://discuss.leetcode.com/topic/31162/mergesort-solution

"""
http://bookshadow.com/weblog/2015/12/06/leetcode-count-of-smaller-numbers-after-self/
解法II 二叉搜索树 （Binary Search Tree）：
树节点TreeNode记录下列信息：

元素值：val
* 小于该节点的元素个数：leftCnt
* leftCnt means the total count of integers in the left subtree of current node
节点自身的元素个数：cnt
左孩子：left
右孩子：right
从右向左遍历nums，在向BST插入节点时顺便做统计
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        bst = BinarySearchTree()
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans

class TreeNode(object):
    def __init__(self, val):
        self.leftCnt = 0
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        root = self.root
        cnt = 0
        while root:
            if val < root.val:
                root.leftCnt += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftCnt + root.cnt
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                cnt += root.leftCnt
                root.cnt += 1
                break
        return cnt
