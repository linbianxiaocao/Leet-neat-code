# http://www.cnblogs.com/grandyang/p/4401196.html

# 理解了解法一和解法二，动态规划的方法更容易理解些
# 解法三有时间再去理解吧，递归返回不同的值是一个思路

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


这道题通配符外卡匹配问题还是小有难度的，有特殊字符 ‘*’ 和 ‘?’，其中 ‘?’ 能代替任何字符，‘*’ 能代替任何字符串，注意跟另一道 Regular Expression Matching 正则匹配的题目区分开来。两道题的星号的作用是不同的，注意对比区分一下。这道题最大的难点，就是对于星号的处理，可以匹配任意字符串，简直像开了挂一样，就是说在星号对应位置之前，不管你s中有任何字符串，我大星号都能匹配你，主角光环啊。但即便叼如斯的星号，也有其处理不了的问题，那就是一旦p中有s中不存在的字符，那么一定无法匹配，因为星号只能增加字符，不能消除字符，再有就是星号一旦确定了要匹配的字符串，对于星号位置后面的匹配情况也就鞭长莫及了。所以p串中星号的位置很重要，用jStar来表示，还有星号匹配到s串中的位置，使用iStart来表示，这里 iStar 和 jStar 均初始化为-1，表示默认情况下是没有星号的。然后再用两个变量i和j分别指向当前s串和p串中遍历到的位置。

开始进行匹配，若i小于s串的长度，进行while循环。若当前两个字符相等，或着p中的字符是问号，则i和j分别加1。若p[j] 是星号，那么我们要记录星号的位置，pStar赋为j，此时j再自增1，iStar赋为i。若当前p[j] 不是星号，并且不能跟p[i] 匹配上，那么此时就要靠星号了，若之前星号没出现过，那么就直接跪，比如 s = "aa" 和 p = "c*"，此时 s[0] 和 p[0] 无法匹配，虽然p[1] 是星号，但还是跪。如果星号之前出现过，可以强行续一波命，比如 s = "aa" 和 p = "*c"，当发现 s[1] 和 p[1] 无法匹配时，但是好在之前 p[0] 出现了星号，我们把 s[1] 交给 p[0] 的星号去匹配。至于如何知道之前有没有星号，这时就能看出 iStar 的作用了，因为其初始化为-1，而遇到星号时，其就会被更新为i，那么我们只要检测 iStar 的值，就能知道是否可以使用星号续命。虽然成功续了命，匹配完了s中的所有字符，但是之后我们还要检查p串，此时没匹配完的p串里只能剩星号，不能有其他的字符，将连续的星号过滤掉，如果j不等于p的长度，则返回false，参见代码如下：

class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, iStar = -1, jStar = -1;
        while (i < s.size()) {
            if (s[i] == p[j] || p[j] == '?') {
                ++i; ++j;
            } else if (p[j] == '*') {
                iStar = i;
                jStar = j++;
            } else if (iStar >= 0) {
                i = ++iStar;
                j = jStar + 1;
            } else return false;
        }
        while (p[j] == '*') ++j;
        return j == p.size();
    }
};

这道题也能用动态规划Dynamic Programming来解，写法跟之前那道题 Regular Expression Matching 很像，但是还是不一样。外卡匹配和正则匹配最大的区别就是在星号的使用规则上，对于正则匹配来说，星号不能单独存在，前面必须要有一个字符，而星号存在的意义就是表明前面这个字符的个数可以是任意个，包括0个，那么就是说即使前面这个字符并没有在s中出现过也无所谓，只要后面的能匹配上就可以了。而外卡匹配就不是这样的，外卡匹配中的星号跟前面的字符没有半毛钱关系，如果前面的字符没有匹配上，那么直接返回false了，根本不用管星号。而星号存在的作用是可以表示任意的字符串，当然只是当匹配字符串缺少一些字符的时候起作用，当匹配字符串p包含目标字符串s中没有的字符时，将无法成功匹配。

对于这种玩字符串的题目，动态规划Dynamic Programming是一大神器，因为字符串跟其子串之间的关系十分密切，正好适合DP这种靠推导状态转移方程的特性。那么先来定义dp数组吧，我们使用一个二维dp数组，其中 dp[i][j] 表示 s中前i个字符组成的子串和p中前j个字符组成的子串是否能匹配。大小初始化为 (m+1) x (n+1)，加1的原因是要包含dp[0][0] 的情况，因为若s和p都为空的话，也应该返回true，所以也要初始化 dp[0][0] 为true。还需要提前处理的一种情况是，当s为空，p为连续的星号时的情况。由于星号是可以代表空串的，所以只要s为空，那么连续的星号的位置都应该为true，所以我们现将连续星号的位置都赋为true。然后就是推导一般的状态转移方程了，如何更新 dp[i][j]，首先处理比较tricky的情况，若p中第j个字符是星号，由于星号可以匹配空串，所以如果p中的前j-1个字符跟s中前i个字符匹配成功了（dp[i][j-1] 为true）的话，那么 dp[i][j] 也能为true。或者若 p中的前j个字符跟s中的前i-1个字符匹配成功了（dp[i-1][j] 为true）的话，那么 dp[i][j] 也能为true（因为星号可以匹配任意字符串，再多加一个任意字符也没问题）。若p中的第j个字符不是星号，对于一般情况，我们假设已经知道了s中前i-1个字符和p中前j-1个字符的匹配情况（即 dp[i-1][j-1] ），那么现在只需要匹配s中的第i个字符跟p中的第j个字符，若二者相等（s[i-1] == p[j-1]），或者p中的第j个字符是问号（p[j-1] == '?'），再与上 dp[i-1][j-1] 的值，就可以更新 dp[i][j] 了，参见代码如下：

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        for (int i = 1; i <= n; ++i) {
            if (p[i - 1] == '*') dp[0][i] = dp[0][i - 1];
        }
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                } else {
                    dp[i][j] = (s[i - 1] == p[j - 1] || p[j - 1] == '?') && dp[i - 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }
};
