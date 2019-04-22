# https://blog.csdn.net/roufoo/article/details/87915863

There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.
---------------------
作者：青灯照壁夜读书
来源：CSDN
原文：https://blog.csdn.net/roufoo/article/details/87915863
版权声明：本文为博主原创文章，转载请附上博文链接！

思路：把两个选手当成1个人，每次都让自己面对剩下的棋子选择最优局面。
sums[i]:从i到len-1的values之和。
dp[i]: 第i轮时，该选手在该轮到比赛结束所能取得的最多coin。
关键代码：
dp[i] = max(sums[i + 1] - dp[i + 1] + values[i],
        sums[i + 2] - dp[i + 2] + values[i] + values[i + 1]);
因为第i轮时，该选手可取1个或2个。若取1个，对手下一轮到比赛结束所能取得的最多coin是dp[i + 1]，所以自己下一轮到比赛结束所取得的最多coin是sums[i + 1] - dp[i + 1]，同时加上这一轮所取的values[i]。若取2个，情况类似。

注意: 该DP要从后往前推，最后判断sums[0] - dp[0] < dp[0]。因为dp[len - 1]和dp[len - 2]好算。
