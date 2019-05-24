#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

// 1. FenwickTree / Binary Indexed Tree
// https://zxi.mytechroad.com/blog/sp/fenwick-tree-binary-indexed-tree-sp3/
// http://zxi.mytechroad.com/blog/data-structure/307-range-sum-query-mutable/
class FenwickTree {
public:
    FenwickTree(int n): sums_(n + 1, 0) {}
    
    void update(int i, int delta) {
        while (i < sums_.size()) {
            sums_[i] += delta;
            i += lowbit(i);
        }
    }
    
    int query(int i) const {
        int sum = 0;
        while (i > 0) {
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }    
private:
    static inline int lowbit(int x) {
        return x & (-x);
    }
    vector<int> sums_;
};

class NumArray {
public:
    NumArray(vector<int>& nums): nums_(std::move(nums)), tree_(nums_.size()) {
        for (int i = 0; i < nums_.size(); ++i)
            tree_.update(i+1, nums_[i]);
    }
    
    void update(int i, int val) {
        tree_.update(i+1, val-nums_[i]);
        nums_[i] = val;
    }
    
    int sumRange(int i, int j) {
        return tree_.query(j+1) - tree_.query(i);
    }
private:
    vector<int> nums_;
    FenwickTree tree_;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */


// 2. Segment Tree
// https://zxi.mytechroad.com/blog/sp/segment-tree-sp14/
// http://zxi.mytechroad.com/blog/data-structure/307-range-sum-query-mutable/
class SegmentTreeNode {
public:
    SegmentTreeNode(int start, int end, int sum,
                    SegmentTreeNode *left = nullptr,
                    SegmentTreeNode *right = nullptr):
        start(start), end(end), sum(sum), left(left), right(right) {}
    SegmentTreeNode(const SegmentTreeNode&) = delete;
    SegmentTreeNode& operator=(const SegmentTreeNode&) = delete;
    ~SegmentTreeNode() {
        delete left;
        delete right;
        left = right = nullptr;
    }

    int start;
    int end;
    int sum;
    SegmentTreeNode *left;
    SegmentTreeNode *right;
};

class NumArray {
public:
    NumArray(vector<int>& nums): nums_(move(nums)) {
        if (!nums_.empty()) root_.reset(buildTree(0, nums_.size() - 1));
    }

    void update(int i, int val) {
        updateTree(root_.get(), i, val);
    }

    int sumRange(int i, int j) {
        return sumRange(root_.get(), i, j);
    }

private:
    vector<int> nums_;
    unique_ptr<SegmentTreeNode> root_;

    SegmentTreeNode* buildTree(int start, int end) {
        if (start == end) return new SegmentTreeNode(start, end, nums_[start]);
        int mid = start + (end - start) / 2;
        auto left = buildTree(start, mid);
        auto right = buildTree(mid + 1, end);
        auto node = new SegmentTreeNode(start, end, left->sum + right->sum,
                                        left, right);
        return node;
    }

    void updateTree(SegmentTreeNode *root, int i, int val) {
        if (root->start == i && root->end == i) {
            root->sum = val;
            return;
        }
        int mid = root->start + (root->end - root->start) / 2;
        if (i <= mid) updateTree(root->left, i, val);
        else updateTree(root->right, i, val);
        root->sum = root->left->sum + root->right->sum;
    }

    int sumRange(SegmentTreeNode* root, int i, int j) {
        if (i == root->start && j == root->end) return root->sum;
        int mid = root->start + (root->end - root->start) / 2;
        if (j <= mid) return sumRange(root->left, i, j);
        else if (i > mid) return sumRange(root->right, i, j);
        else return sumRange(root->left, i, mid) + sumRange(root->right, mid+1, j);
    }

};