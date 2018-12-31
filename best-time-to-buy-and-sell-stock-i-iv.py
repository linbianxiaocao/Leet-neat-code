i and ii are easy

# iii: https://www.cnblogs.com/zuoyuan/p/3766168.html
解题思路：只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。

note: very smart, just by breaking the array into two parts, and iterate through all possible partitions

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


