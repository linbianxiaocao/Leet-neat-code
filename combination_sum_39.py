# https://blog.csdn.net/fuxuemingzhu/article/details/79322462

dfs搜索，先对所有的值进行排序，然后对每个元素进行dfs搜索，判断能否得到target。用了几个条件判断进行提前终止，这样能加速。

# jie note, sorting is helpful
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

