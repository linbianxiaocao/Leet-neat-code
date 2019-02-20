# http://www.cnblogs.com/grandyang/p/5278930.html


ven a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]


这道题让我们竖直遍历二叉树，并把每一列存入一个二维数组，我们看题目中给的第一个例子，3和15属于同一列，3在前，第二个例子中，3,5,2在同一列，3在前，5和2紧随其后，那么我们隐约的可以感觉到好像是一种层序遍历的前后顺序，那么我们如何来确定列的顺序呢，我们可以把根节点给个序号0，然后开始层序遍历，凡是左子节点则序号减1，右子节点序号加1，这样我们可以通过序号来把相同列的节点值放到一起，我们用一个TreeMap来建立序号和其对应的节点值的映射，用TreeMap的另一个好处是其自动排序功能可以让我们的列从左到右，由于层序遍历需要用到queue，我们此时queue里不能只存节点，而是要存序号和节点组成的pair，这样我们每次取出就可以操作序号，而且排入队中的节点也赋上其正确的序号，代码如下：

class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        map<int, vector<int>> m;
        queue<pair<int, TreeNode*>> q;
        q.push({0, root});
        while (!q.empty()) {
            auto a = q.front(); q.pop();
            m[a.first].push_back(a.second->val);
            if (a.second->left) q.push({a.first - 1, a.second->left});
            if (a.second->right) q.push({a.first + 1, a.second->right});
        }
        for (auto a : m) {
            res.push_back(a.second);
        }
        return res;
    }
};
