# https://blog.csdn.net/fuxuemingzhu/article/details/79322462

dfs搜索，先对所有的值进行排序，然后对每个元素进行dfs搜索，判断能否得到target。用了几个条件判断进行提前终止，这样能加速。

# jie note, sorting能加速递归提前终止(剪枝)，但不sorting也能pass
# 用index记录从哪个数开始加，避免重复

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res


    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])

e.g.,
dfs([2, 3, 5, 7], 7) ->
    dfs([2, 3, 5, 7], 5)
    dfs([3, 5, 7], 4)
    dfs([5, 7], 2)
    dfs([7], 0)


c++
class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/4419259.html
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(candidates, target, 0, res, path);
        return res;
    }
    
    void dfs(vector<int>& nums, int target, int index, vector<vector<int>>& res, vector<int>& path) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = index; i < nums.size(); ++i) {
            path.push_back(nums[i]);
            dfs(nums, target-nums[i], i, res, path);
            path.pop_back();
        }
    }
};

class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/4419259.html
    // with sorting
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, res, path);
        return res;
    }
    
    void dfs(vector<int>& nums, int target, int index, vector<vector<int>>& res, vector<int>& path) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
            return;
        }
        if (nums[index] > target) return;
        for (int i = index; i < nums.size(); ++i) {
            path.push_back(nums[i]);
            dfs(nums, target-nums[i], i, res, path);
            path.pop_back();
        }
    }
};