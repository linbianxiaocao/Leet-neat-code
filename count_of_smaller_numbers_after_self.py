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
# Solution 1: The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left jumps.
#https://discuss.leetcode.com/topic/31162/mergesort-solution
def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller


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

# c++
# http://www.cnblogs.com/grandyang/p/5078490.html
1. BST
    int insert(Node *&root, int v) {
        if (!root) return (root = new Node(v, 0)), 0;
        if (root->val > v)
            return root->smaller++, insert(root->left, v);
        else
            return insert(root->right, v)+root->smaller+(root->val<v?1:0);
    }

    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res(nums.size());
        Node *root = NULL;
        for (int i = nums.size()-1; i>=0; --i) {
            res[i] = insert(root, nums[i]);
        }
        return res;
    }

# 1.1 BST huahua: https://zxi.mytechroad.com/blog/algorithms/array/leetcode-315-count-of-smaller-numbers-after-self/
struct BSTNode {
    int val, count, left_count;
    BSTNode* left, right;
    BSTNode(int val): val(val), count(1), left_count(0), 
        left(nullptr), right{nullptr} {}
    ~BSTNode() {delete left; delete right; }
    int less_or_equal() const {return count + left_count;}
};
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        if (nums.empty()) return {};
        std::reverse(nums.begin(), nums.end());
        std::unique_ptr<BSTNode> root(new BSTNode(nums[0]));
        vector<int> ans{0};
        for (int i = 1; i < nums.size(); ++i)
            ans.push_back(insert(root.get(), nums[i]));
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
private:
    int insert(BSTNode* root, int val) {
        if (root->val == val) {
            ++root->count;
            return root->left_count;
        } else if (val < root->val) {
            ++root->left_count;
            if (root->left == nullptr) {
                root->left = new BSTNode(val);
                return 0;
            }
            return insert(root->left, val);
        } else {
            if (root->right == nullptr) {
                root->right = new BSTNode(val);
                return root->less_or_equal();
            }
            return root->less_or_equal() + insert(root->right, val);
        }
    }
};



2.
// Insert Sort
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> t, res(nums.size());
        for (int i = nums.size() - 1; i >= 0; --i) {
            int d = distance(t.begin(), lower_bound(t.begin(), t.end(), nums[i]));
            res[i] = d;
            t.insert(t.begin() + d, nums[i]);
        }
        return res;
    }
};

3. BinaryIndexedTree (Fenwick Tree)
https://zxi.mytechroad.com/blog/algorithms/array/leetcode-315-count-of-smaller-numbers-after-self/

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        // Sort the unique numbers
        set<int> sorted(nums.begin(), nums.end());
        // Map the number to its rank
        unordered_map<int, int> ranks;
        int rank = 0;
        for (const int num : sorted)
            ranks[num] = ++rank;
        
        vector<int> ans;
        FenwickTree tree(ranks.size());
        // Scan the numbers in reversed order
        for (int i = nums.size() - 1; i >= 0; --i) {
            // Chechk how many numbers are smaller than the current number.
            ans.push_back(tree.query(ranks[nums[i]] - 1));
            // Increse the count of the rank of current number.
            tree.update(ranks[nums[i]], 1);
        }
        
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};

4. bisect to maintain a sorted list
import bisect
class Solution(object):
    def countSmaller(self, nums):
        result = []
        sortedList = []
        for num in nums[::-1]:
            position = bisect.bisect_left(sortedList, num)
            result.append(position)
            sortedList.insert(position, num)
        return result[::-1]


