Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
	res = ""
	left, cnt, minLen = 0, 0, float('inf')
	count = collections.Counter(t)
	for i, c in enumerate(s):

# 重点行
	    count[c] -= 1
 	    if count[c] >= 0:
                cnt += 1
#
            if cnt < len(t):
		continue
	    // 这时候cnt == len(t)
            while cnt == len(t): // 找到一个合格的区间
                if i - left + 1 < minLen:
                    minLen = i - left + 1
                    res = s[left:i+1]
# 重点行
                count[s[left]] += 1
                if count[s[left]] > 0:
	            cnt -= 1
#
	        left += 1               // 收缩左指针
       return res


// 直观的想法感觉不是太难，但实现起来还是有道道的，特别要理解cnt这个变量
// 有难度，需要仔细研究

// https://blog.csdn.net/fuxuemingzhu/article/details/82931106
统计字符出现的个数，而且时间复杂度要求O(N)，明显使用双指针解题。和567. Permutation in String有点相似，都是要求子字符串满足一定的次数要求。

使用right指针向右搜索，同时要记录在left～right这个区间内包含的T中每个元素出现的个数和。如果在[left,right]区间内，元素出现的个数和与T长度相等了，说明在这个区间是符合要求的一个区间，但是不一定是最短区间。

因此，现在要移动left指针，要求，在[left, right]区间内的元素出现个数应该把T中所有的元素都包含。同样使用cnt来验证是否包含了T所有的元素。cnt的含义是在s[left, right]区间内，和t的相等的字符个数统计。cnt是个很重要的变量，它是来维护左右指针的参考。

在移动left指针的时候要注意存储最短的子串，当所有的循环都结束之后最短字符串即为题目要求了。使用的minLen变量即当前满足题目要求的最短子串长度，要返回的结果res根据minLen和当前的满足题目要求的子串长度进行比较从而更新。

这个题难点就在于维护cnt，其实如果使用普通的求T的元素个数是不是S[left, right]的元素子集的方法应该更容易理解，但是不知道能不能通过OJ。这个思路比较重要，其他都还好。

时间复杂度是O(N)，空间复杂度是O(N)。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82931106
版权声明：本文为博主原创文章，转载请附上博文链接！
