# https://blog.csdn.net/fuxuemingzhu/article/details/79343638
这个题和之前的39. Combination Sum 基本相同，这个题不允许一个数字多次出现，所以每次递归需要比上一轮开始的位置向后移动一个。

另外这个题一直做不出来的原因是把dfs的i写成了index…要注意内层递归的时候，传入的位置是i不是index.

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        print(candidates)
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            # prevent duplication
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])


class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/4419386.html
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
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
        for (int i = index; i < nums.size(); ++i) {
            if (i > index && nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            dfs(nums, target-nums[i], i+1, res, path);
            path.pop_back();
        }
    }
};

