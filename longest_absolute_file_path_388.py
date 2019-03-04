https://blog.csdn.net/fuxuemingzhu/article/details/82841402

解题方法
第一个感觉DFS、或者栈。估计这两种方法都可以，我是使用栈做的，没想到这么简单就过了，难度在哪里。。

使用一个栈同时保存目录的深度，当前总的字符串长度，那么：

计算当前目录的深度，如果当前深度小于栈的深度，那么把栈弹出来到比当前浅为止。如果当前遍历到的是目录，如果大于栈中最上面目录的深度，那么进栈；如果当前遍历的是文件，那么统计总的深度即可。

需要注意的是，目录是需要分隔符的，所以目录进栈的深度应该是目录深度+1。

时间复杂度是O(N)，空间复杂度是O(N). N为input按照"\n"分割后的个数。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82841402
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = [(-1, 0)] # 目录的深度，当前总的字符串长度
        max_len = 0
        for p in input.split("\n"):
            depth = p.count('\t')
            p = p.replace('\t', '')
            while stack and depth <= stack[-1][0]: # 一样深，或者当前目录更浅
                stack.pop()
            if '.' not in p: # 目录
                stack.append((depth, len(p) + stack[-1][1] + 1))
            else: # 文件
                max_len = max(max_len, len(p) + stack[-1][1])
        return max_len

