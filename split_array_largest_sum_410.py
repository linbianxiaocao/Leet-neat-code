# 1. DP
    # https://www.cnblogs.com/grandyang/p/5933787.html
# 其中dp[i][j]表示将数组中前j个数字分成i组所能得到的最小的各个子数组中最大值
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        sums = [0] * (n+1)
        dp = [[float('inf') for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = 0

        for i in range(1,n+1):
            sums[i] = sums[i-1]+nums[i-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(i-1, j): # i-1 <= k <= j-1
                    val = max(dp[i-1][k], sums[j]-sums[k])
                    dp[i][j] = min(dp[i][j], val)

        return dp[m][n]

2. binary
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, 0
        for i in range(n):
            left = max(left, nums[i])
            right += nums[i]

        while left < right:
            mid = left+(right-left)/2
            if self.canSplit(nums, m, mid):
                right = mid
            else:
                left = mid+1
        return left

    def canSplit(self, nums, m, sum):
        cnt = 1
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum>sum:
                currSum = nums[i]
                cnt += 1
                if cnt>m:
                    return False
        return True
