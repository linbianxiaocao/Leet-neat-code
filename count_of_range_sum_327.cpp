class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/5162678.html
    // sums = [0, a0, a0+a1, a0+a1+a2, ...]
    // range_sum[i,j] = sums[j+1] - sums[i], where 0<=i<=j<=n-1
    // so, sums[j+1]-upper <= sums[i] <= sums[j+1]-lower
    // e.g., when j = 0, a0-upper <= sum[i] <= a0-lower, i = 0
    // when j = 1, a0+a1-upper <= sums[i] <= a0+a1-lower, i = 0, 1
    // when j = 2, a0+a1+a2-upper <= sums[i] <= a0+a1+a2-lower, i = 0, 1, 2
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int res = 0;
        long sum = 0;
        multiset<long> sums;
        sums.insert(0);
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            res += distance(sums.lower_bound(sum-upper), sums.upper_bound(sum-lower));
            sums.insert(sum);
        }
        return res;
    }
};


// BIT解法：http://bookshadow.com/weblog/2016/01/11/leetcode-count-of-range-sum/


class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/5162678.html
    // nice explanation in https://leetcode.com/problems/count-of-range-sum/discuss/77990/Share-my-solution
    // sums = [0, a0, a0+a1, a0+a1+a2, ...]
    // range_sum[i,j] = sums[j+1] - sums[i], where 0<=i<=j<=n-1
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        vector<long> sums(nums.size()+1, 0);
        for (int i = 0; i < nums.size(); ++i) sums[i+1] = sums[i]+nums[i];
        return countAndMergeSort(sums, 0, sums.size(), lower, upper);
    }
    
    // sums[start], sums[start+1], ..., sums[end-1]
    // so only meaningful when end-1>start
    // 左闭右开的区间：[start, end)
    int countAndMergeSort(vector<long>& sums, int start, int end, int lower, int upper) {
        if (end - start <= 1) return 0;
        int mid = start + (end - start) / 2;
        int cnt = countAndMergeSort(sums, start, mid, lower, upper) 
            + countAndMergeSort(sums, mid, end, lower, upper);
        
        int j = mid, k = mid, t = mid;
        vector<int> cache(end-start, 0);
        for (int i = start, r = 0; i < mid; ++i, ++r) {
            while (k < end && sums[k]-sums[i] < lower) ++k;
            while (j < end && sums[j]-sums[i] <= upper) ++j;
            cnt += j - k;
            while (t < end && sums[t] < sums[i]) cache[r++] = sums[t++];
            cache[r] = sums[i];
        }
        copy(cache.begin(), cache.begin()+t-start, sums.begin()+start);
        return cnt;
    }
};
