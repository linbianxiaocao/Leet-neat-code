# https://www.youtube.com/watch?v=IFNibRVgFBo

https://www.cnblogs.com/grandyang/p/5006441.html

Assume k is the last balloon to burst in the subarray of [i, j]
[i, ..., k-1, k, k+1, ..., j]
dp[i, j] = max(dp[i, k-1] + dp[k+1, j] + nums[i-1] * nums[k] * nums[j+1] for k in [i, j])
