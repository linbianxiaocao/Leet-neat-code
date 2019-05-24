#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;
//1. TLE的二分法 http://www.cnblogs.com/grandyang/p/5434414.html
// search i < j, nums[i] > nums[j]
int reversePairs_1(vector<int>& nums) {
    int res = 0;
    vector<int> t;
    for (int i = nums.size()-1; i >= 0; --i) {
        int left = 0, right = t.size();
        while (left < right) {
            // find smallest index in t, such that t[index] >= nums[i]
            int mid = left + (right - left) / 2;
            if (t[mid] >= nums[i]) right = mid;
            else left = mid + 1;
        }
        t.insert(t.begin() + left, nums[i]);
        res += left;
    }
    return res;
}

// 于是我就开始稍稍改了一下，二分搜索的时候是搜索nums[i]/2.0，加入数组的时候是加入原数num。
// 我记得当时是可以通过OJ的，但是后来OJ变的严格起来了
// search i < j, nums[i] > 2*nums[j]
int reversePairs_1_1(vector<int>& nums) {
    int res = 0;
    vector<int> t;
    for (int i = nums.size()-1; i >= 0; --i) {
        int left = 0, right = t.size();
        while (left < right) {
            // find smallest index in t, such that t[index] >= nums[i]/2.0
            int mid = left + (right - left) / 2;
            if (t[mid] >= nums[i]/2.0) right = mid;
            else left = mid + 1;
        }
        res += left;

        vector<int>::iterator lbi = lower_bound(t.begin(), t.end(), nums[i]);
        int d = distance(t.begin(), lbi);
        t.insert(t.begin() + d, nums[i]);
    }
    return res;
}

// 2. Partition Recurrence Relation
// https://www.cnblogs.com/grandyang/p/6657956.html
// https://www.youtube.com/watch?v=j68OXAMlTM4
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        return mergeSort(nums, 0, nums.size()-1);
    }
    
    int mergeSort(vector<int>& nums, int left, int right) {
        if (left >= right) return 0;
        int mid = left + (right - left) / 2;
        int res = mergeSort(nums, left, mid) + mergeSort(nums, mid+1, right);

        int i = left, j = mid+1;
        while (i <= mid && j <= right) {
            if (nums[i]/2.0 > nums[j]) {
                res += mid - i + 1;
                j++;
            }
            else i++;
        }

        merge(nums, left, mid, right);
        // sort(nums.begin() + left, nums.begin() + right + 1);
        return res;
    }

    void merge(vector<int>& nums, int left, int mid, int right) {
        vector<int> temp(right-left+1);
        int i = left, j = mid + 1, k = 0;

        // merge the two parts into temp
        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) temp[k++] = nums[i++];
            else temp[k++] = nums[j++];
        }
        // insert all the remaining values from i to mid, j to right into temp
        while (i <= mid) temp[k++] = nums[i++];
        while (j <= right) temp[k++] = nums[j++];

        // assign sorted data stored in temp to nums
        for (i = left; i <= right; ++i) nums[i] = temp[i-left];
    }
};

// 3. Sequential recurrence relation - 1. BST - based solution
// https://leetcode.com/problems/reverse-pairs/discuss/97268/general-principles-behind-problems-similar-to-reverse-pairs
// Note: this homemade BST is not self-balanced and the time complexity can go as bad as O(n^2) (in fact you will get TLE if you copy and paste the solution here). 
// To guarantee O(nlogn) performance, use one of the self-balanced BST's (e.g. Red-black tree, AVL tree, etc.).
struct Node {
    //cnt is the total number of elements in the subtree of current node that >= val
    int val, cnt;   
    Node *left, *right;
    Node(int val) : val(val), cnt(1), left(NULL), right(NULL) {}
};

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int res = 0;
        Node *root = NULL;
        for (int n : nums) {
            // 和之前的二分法比较，这里是找2倍的当前值，之前是找当前值的一半（int不会overflow）
            res += search(root, 2L * n + 1);
            root = insert(root, n);
        }
        return res;
    }

private:
    Node* insert(Node *root, int val) {
        if (!root) return new Node(val);
        if (val == root->val) root->cnt++;
        else if (val < root->val) root->left = insert(root->left, val);
        else {
            root->cnt++;
            root->right = insert(root->right, val);
        }
        return root;
    }

    // search val and return the number of nodes in tree that >= val
    int search(Node *root, long val) {   
        if (!root) return 0;
        if (val == root->val) return root->cnt;
        else if (val < root->val) return root->cnt + search(root->left, val);
        else return search(root->right, val);
    }
};

// 3. Sequential recurrence relation - 1. BIT - based solution
// https://leetcode.com/problems/reverse-pairs/discuss/97268/general-principles-behind-problems-similar-to-reverse-pairs
class Solution {
public:
//     https://www.cnblogs.com/grandyang/p/6657956.html
//     BIT
//     similar solution with BIT for https://zxi.mytechroad.com/blog/algorithms/array/leetcode-315-count-of-smaller-numbers-after-self/
    int reversePairs(vector<int>& nums) {
        int res = 0, n = nums.size();
        vector<int> v = nums, bit(n + 1);
        sort(v.begin(), v.end());
        unordered_map<int, int> m; // ranks
        for (int i = 0; i < n; ++i) m[v[i]] = i + 1;
        for (int i = n-1; i >= 0; --i) {
            vector<int>::iterator lbi = lower_bound(v.begin(), v.end(), nums[i] / 2.0);
            res += getSum(lbi - v.begin(), bit);
            update(m[nums[i]], bit);
        }
        return res;
    }
    
    int getSum(int i, vector<int>& bit) {
        int sum = 0;
        while (i > 0) {
            sum += bit[i];
            i -= (i & -i);
        }
        return sum;
    }
    
    void update(int i, vector<int>& bit) {
        while (i < bit.size()) {
            bit[i] += 1;
            i += (i & -i);
        }
    }
};