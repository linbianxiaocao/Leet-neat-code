18. 可乐饮料机 高频 5次
有一系列按钮，每个按钮按下去会得到一定体积范围的可乐。先给定一个目标体积范围，问不限制按按钮次数，能否确定一定能得到目标范围内的可乐？

举例：有三个按钮，按下去得到的范围是[100, 120], [200, 240], [400, 410],

假设目标是[100, 110], 那答案是不能。因为按下一，可能得到120体积的可乐，不在目标范围里。

假设目标是[90, 120]，那答案是可以。因为按下一，一定可以得到此范围内的可乐。

假设目标是[300, 360], 那答案是可以，因为按下一再按二，一定可以得到此范围内

[bq]
假设目标是[310, 360], 那答案是不能，因为按下一再按二，有可能得到300，永远没可能确定得到这个范围内的可乐。

假设目标是[1, 9999999999]，那答案是可以。随便按一个都确定满足此范围。

思路：dfs+memorization从0开始暴力解  一开始[0, 0] 通过bfs、dfs往上加直到出界[br]

public static boolean dfs(List<Soda> sodas, int volumeLower, int volumeUpper,

                              int targetLower, int targetUpper, Map<String, Boolean> memo) {

[bs]


        Boolean val = memo.get(volumeLower + "-" + volumeUpper);

        if (val != null) {

            return val;

        }



        if (volumeLower >= targetLower && volumeUpper <= targetUpper) {

            return true;

        }

        if (volumeUpper > targetUpper) {

            return false;[bt][bu][bv]

        }

         // if (volumeUpper - volumeLower > targetUpper - targetLower) retuurn false;

        for (Soda soda : sodas) {

            if (dfs(sodas, volumeLower + soda.lower, volumeUpper + soda.upper, targetLower, targetUpper, memo)) {//false的子问题会重复计算

                memo.put(volumeLower + "-" + volumeUpper, true);

                return true;

            }

        }



        memo.put(volumeLower + "-" + volumeUpper, false);

        return false;

    }

据说这题是binary search？  这个应该bfs，dfs都能做。但是据说还可以用dp，dp怎么做啊。谁能po个解法？

区间DP的做法：(Provider: anonym)
public static boolean coke(List<List<Integer>> buttons, List<Integer> target) {

    int m = target.get(0);

    int n = target.get(1);

    boolean[][] dp = new boolean[m + 1][n + 1];



    //Init

    for (int i = 0; i <= m; ++i) {

      for (int j = 0; j <= n; ++j) {

        for (List<Integer> button: buttons) {

          if (i <= button.get(0) && j >= button.get(1)) {[bw][bx]

            dp[i][j] = true;

            break;[by]

          }

        }

      }

    }



    for (int i = 0; i <= m; ++i) {

      for (int j = 0; j <= n; ++j) {

        for (List<Integer> button: buttons) {

          int preL = i - button.get(0);

          int preR = j - button.get(1);[bz][ca]

          if (preL >= 0 && preR >= 0 && dp[preL][preR]) {

            dp[i][j] = true;

           break;

          }

        }

      }

    }



    return dp[m][n];

  }

这算是一个多重背包问题。我曾经被面到过一个类似的：给一个调色板由一堆颜色组成，每个颜色有RGB三个分量。问能否调出一个目标颜色
