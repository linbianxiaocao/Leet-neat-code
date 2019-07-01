i and ii are easy

# iii: https://www.cnblogs.com/zuoyuan/p/3766168.html
解题思路：只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。

note: very smart, just by breaking the array into two parts, and iterate through all possible partitions

c++
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) return 0;
        int n = prices.size();
        //f1[i]表示在price[i]之前进行一次交易所获得的最大利润(包括i)，f2[i]表示在price[i]之后进行一次交易所获得的最大利润(不包括i)
        int f1[n] = {0}, f2[n] = {0};

        int lowest_price = prices[0];
        for (int i = 1; i < n; ++i) {
            f1[i] = max(f1[i-1], prices[i]-lowest_price);
            lowest_price = min(lowest_price, prices[i]);
        }

        int max_price = prices[n-1];
        for (int i = n-2; i >= 1; --i) {
            f2[i-1] = max(f2[i], max_price-prices[i]);
            max_price = max(max_price, prices[i]);
        }

        int res = 0;
        for (int i = 0; i < n; ++i)
            res = max(res, f1[i] + f2[i]);

        return res;
    }

# iv: https://blog.csdn.net/qq508618087/article/details/51678245
思路：当k >= len/2时，问题就退化成了可以交易任意次了，所以只要将任意两天股票差大于０的加起来即可．

当k < len/2时，可以记录k次交易每次买之后和卖以后最大的利润：

１．第ｉ次买操作买下当前股票之后剩下的最大利润为第(i-1)次卖掉股票之后的利润－当前的股票价格．状态转移方程为：

　　　　buy[i] = max(sell[i-1]- curPrice, buy[i]);

２．第ｉ次卖操作卖掉当前股票之后剩下的最大利润为第ｉ次买操作之后剩下的利润＋当前股票价格．状态转移方程为：

　　　　sell[i] = max(buy[i]+curPrice, sell[i]);
---------------------
作者：小榕流光
来源：CSDN
原文：https://blog.csdn.net/qq508618087/article/details/51678245
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if(prices.size() ==0) return 0;
        int len = prices.size(), ans =0　;
        if(k >= len/2)
        {
            for(int i = 1; i < len; i++)
                if(prices[i]-prices[i-1])>0) ans += prices[i]-prices[i-1];
            return ans;
        }
        vector<int> buy(len+1, INT_MIN), sell(len+1, 0);
        for(auto val: prices)
        // 动态规划， 每次assume之前的buy[0:k+1], sell[0:k+1]数组已经是最优，遍历完prices即是全局最优
        {
            for(int i =1; i <= k; i++)
            {
                buy[i] = max(sell[i-1]-val, buy[i]);
                sell[i] = max(buy[i]+val, sell[i]);
            }
        }
        return sell[k];
    }
};
以上方法是先循环次数，再循环天数

# Tushar explanation very well
https://www.youtube.com/watch?v=oDhu5uGq_ic

ith transaction, jth day
先循环天数，再循环次数
T[i][j] = max(
    T[i][j-1], # no transaction on jth day
    T[i-1][m] + price[j]-price[m], # buy at mth day, sell at jth day, for m = 0, 1, j-1
                                   # this will cover sell at mth day, buy at mth day again, but it's a case that won't matter for the result
                                   # Tushar showed the for loop (m=0,1,..j-1) can be optimized in constant time
    )

optimized:
T[i][j] = max(
        T[i][j-1],
        price[j] + maxDiff where maxDiff = max(maxDiff, T[i-1][j]-p[j])


https://www.cnblogs.com/grandyang/p/4295761.html
但这道题还有个坑，就是如果k的值远大于prices的天数，比如k是好几百万，而prices的天数就为若干天的话，上面的DP解法就非常的没有效率，应该直接用Best Time to Buy and Sell Stock II 买股票的最佳时间之二的方法来求解，所以实际上这道题是之前的二和三的综合体，代码如下：


class Solution {
public:
    // tushar: https://www.youtube.com/watch?v=oDhu5uGq_ic
    // slower method but easier to understand    
// T[i][j] = max(
//     T[i][j-1], # no transaction on jth day
//     T[i-1][m] + price[j]-price[m], # buy at mth day, sell at jth day, for m = 0, 1, j-1
//                                    # this will cover sell at mth day, buy at mth day again, but it's a case that won't matter for the result
//                                    # Tushar showed the for loop (m=0,1,..j-1) can be optimized in constant time
//     )    
// O(k * n2)
    int maxProfit(int k, vector<int>& prices) {
        if (k == 0 || prices.empty()) return 0;
        int n = prices.size();
        
        if (k >= n) return solveMaxProfit(prices);

        vector<vector<int>> dp(k+1, vector<int>(n, 0));
        for (int i = 1; i <= k; ++i) {
            for (int j = 1; j <= n-1; ++j) {
                int max_val = 0;
                for (int m = 0; m <= j-1; ++m)
                    max_val = max(max_val, prices[j] - prices[m] + dp[i-1][m]);
                dp[i][j] = max(max_val, dp[i][j-1]);   
            }            
        }
        return dp[k][n-1];
    }
    
    int solveMaxProfit(vector<int> &prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] - prices[i - 1] > 0) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }    
};



class Solution {
public:
    // tushar: https://www.youtube.com/watch?v=oDhu5uGq_ic
    // faster method O(k * n)
    int maxProfit(int k, vector<int>& prices) {
        if (k == 0 || prices.empty()) return 0;
        int n = prices.size();
        
        if (k >= n) return solveMaxProfit(prices);        
        
        vector<vector<int>> dp(k+1, vector<int>(n, 0));
        for (int i = 1; i <= k; ++i) {
            int max_diff = -prices[0];
            for (int j = 1; j <= n-1; ++j) {
                dp[i][j] = max(dp[i][j-1], max_diff + prices[j]);
                max_diff = max(max_diff, dp[i-1][j] - prices[j]);  
            }            
        }
        return dp[k][n-1];
    }
    
    int solveMaxProfit(vector<int> &prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] - prices[i - 1] > 0) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }       
};


// https://www.cnblogs.com/grandyang/p/4295761.html
// https://blog.csdn.net/linhuanmars/article/details/23236995
// 这么想还是有点复杂的，记录几点帮助理解：
/**
1. 这里使用一维滚动数组优化代替二维数组，特别注意内层循环要从后往前。如果是从前往后，就相当于用第i天的值覆盖了第i-1天的global和local数组，导致后面的计算出错。
2. 递推公式不是很好理解，试图结合这个例子：
day:   0 1 2 3 4
price: 2 8 3 1 9
可见diff = price[4]-price[3] = 8
global[3][1] = 6
local[3][2] = -2+8-3+1 = 4
根据公式得到
local[4][2] = max(-2+8-3+9, 6+8) = 14
同时可见global[3][2] = 6
global[4][2] = max(6, 14) = 14

调整一下例子，再想
day:   0 1 2 3 4
price: 2 8 1 3 9
可见diff = 9-3 = 6
global[3][1] = 6,
local[3][2] = -2+8-1+3 = 8

*/
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (prices.empty()) return 0;
        if (k >= prices.size() / 2) return solveMaxProfit(prices);
        int g[k+1] = {0};
        int l[k+1] = {0};
        for (int i = 0; i < prices.size() - 1; ++i) {
            int diff = prices[i+1] - prices[i];
            for (int j = 1; j <= k; ++j) {
                l[j] = max(g[j-1] + max(diff, 0), l[j] + diff);
                g[j] = max(g[j], l[j]);
            }
        }
        return g[k];
    }
    
    int solveMaxProfit(vector<int>& prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] - prices[i-1] > 0)
                res += prices[i] - prices[i-1];
        }
        return res;
    }
};




