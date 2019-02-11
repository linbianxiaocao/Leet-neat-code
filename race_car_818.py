# https://www.hrwhisper.me/leetcode-dynamic-programming/

# https://blog.csdn.net/magicbean2/article/details/80333734

大概有个思路，2^n粗调步长

思路：

DP,设dp[i]为到达i的最小步数。

则对于i = 2^k – 1，走k步即可（没有更优的了）

对于2^(k-1) < i < 2^k

先走到2^(k-1) – 1处(A^(k-1))，然后掉头，然后走A^x, 然后掉头，走dp[i – (2^(k -1) – 1)+ 2^(x) – 1]，所以总共为k-1 +  1 + x + 1 + dp[i – (2^(k -1) – 1)+ 2^(x) – 1]
走到2^k – 1，然后掉头，走dp[2^k -1 – i]  总共 k + 1+ dp[2^k – 1- target]
