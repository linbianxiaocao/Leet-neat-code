#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

class NumArray {
public:
//     NumArray(vector<int>& nums) {
//         if (nums.size() == 0) return;
//         dp.reserve(nums.size());
//         dp[0] = nums[0];
//         for (int i = 1; i < nums.size(); ++i)
//             dp[i] = nums[i] + dp[i-1];
//     }
    
//     int sumRange(int i, int j) {
//         return i == 0 ? dp[j] : dp[j] - dp[i-1];
//     }
    
// 当然，我们也可以通过增加一位 dp 的长度，来避免在 sumRange 中检测i是否为0，参见代码如下：
// http://www.cnblogs.com/grandyang/p/4952464.html
    NumArray(vector<int> &nums) {
        dp.resize(nums.size() + 1, 0);
        for (int i = 1; i <= nums.size(); ++i)
            dp[i] = dp[i-1] + nums[i-1];
    }
    
    int sumRange(int i, int j) {
        return dp[j+1]-dp[i];
    }
    
private:
    vector<int> dp;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */