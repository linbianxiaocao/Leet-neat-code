i and ii are easy

# iii: https://www.cnblogs.com/zuoyuan/p/3766168.html
解题思路：只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。

note: very smart, just by breaking the array into two parts, and iterate through all possible partitions

