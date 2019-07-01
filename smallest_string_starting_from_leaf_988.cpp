class Solution {
public:
    // huahua: https://zxi.mytechroad.com/blog/tree/leetcode-988-smallest-string-starting-from-leaf/
	// 这个方法有错：递归取min handle不了下面这种情况：b < ba, 然后两边都加了根节点e之后，结果be > bae
    string smallestFromLeaf(TreeNode* root) {
        if (!root) return "|"; 
        const char v = static_cast<char>('a' + root->val);
        if (!root->left && !root->right) return string(1, v);
        string l = smallestFromLeaf(root->left);
        string r = smallestFromLeaf(root->right);
        return min(l, r) + v;
    }
};

class Solution {
public:
    // https://blog.csdn.net/fuxuemingzhu/article/details/87832383
    string smallestFromLeaf(TreeNode* root) {
        vector<string> res{""};
        dfs(root, "", res);
        return res[0];
    }
    
    void dfs(TreeNode* root, string path, vector<string>& res) {
        string one_path = char('a' + root->val) + path;
        if (!root->left && !root->right) {
            if (res[0].empty() || one_path < res[0]) res[0] = one_path;
            return;
        }
        if (root->left) dfs(root->left, one_path, res);
        if (root->right) dfs(root->right, one_path, res);
    }
};


