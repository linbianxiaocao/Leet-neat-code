https://blog.csdn.net/qq508618087/article/details/50811818

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
---------------------
作者：小榕流光
来源：CSDN
原文：https://blog.csdn.net/qq508618087/article/details/50811818
版权声明：本文为博主原创文章，转载请附上博文链接！


思路: 可以用hash表来保存前n个数的和,然后每次去查是否当前和与目标值之差已经存在, 是的话说明我们找到了一个序列,然后更新最大长度大小. 哦, 还有就是如果有相同的和, 那就不管了, 因为我们要的最长的子串, 肯定是留着前面的一个值更优.

jie note,结合560 Subarray Sum Equals K, 同样的思路

class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        if(nums.size()==0) return 0;
        unordered_map<int, int> hash;
        int sum = 0, Max = 0;
        hash[0] = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];
            if(hash.count(sum-k)) Max = max(Max, i-hash[sum-k]+1);
            if(!hash.count(sum)) hash[sum] = i+1;
        }
        return Max;
    }
};
