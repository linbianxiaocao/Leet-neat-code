Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

https://blog.csdn.net/fuxuemingzhu/article/details/82767119

看了数组的长度，明显O(n^2)的时间复杂度会超时。这个时间复杂度一般只能用O(N)的解法了。

使用一个字典保存数组某个位置之前的数组和，然后遍历数组求和，这样当我们求到一个位置的和的时候，向前找sum-k是否在数组中，如果在的话，更新结果为之前的结果+(sum-k出现的次数)。同时，当前这个sum出现的次数就多了一次。

(jie note, 这段写的不是很容易理解，自己通过举例理解)
这个字典的意义是什么呢？其意义就是我们在到达i位置的时候，前i项的和出现的次数的统计。我们想找的是在i位置向前的连续区间中，有多少个位置的和是k。有了这个统计，我们就不用向前一一遍历找sum - k在哪些位置出现了，而是直接得出了前面有多少个区间。所以，在每个位置我们都得到了以这个位置为结尾的并且和等于k的区间的个数，所以总和就是结果。

这个题的解法不难想出来，因为如果要降低时间复杂度，应该能想到增加空间复杂度，那么要么使用数组，要么就是用字典之类的，保留之前的结果。

时间复杂度是O(N)，空间复杂度是O(N).
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82767119
版权声明：本文为博主原创文章，转载请附上博文链接！

https://www.youtube.com/watch?v=mKXIH9GnhgU
example: [1, 1, -1, 1], k = 1, ans = 5


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82767119
版权声明：本文为博主原创文章，转载请附上博文链接！
