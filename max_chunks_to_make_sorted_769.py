class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        pre_max = 0
        for i, num in enumerate(arr):
            if num > pre_max:
                pre_max = num
            if pre_max == i:
                chunks += 1
        return chunks
'''
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80482014
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

分析的不错
https://www.cnblogs.com/grandyang/p/8823944.html
