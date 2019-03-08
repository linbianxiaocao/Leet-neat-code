# https://blog.csdn.net/fuxuemingzhu/article/details/82469175

回溯法
刚开始感觉到很难，是因为没有建立好模型，这个其实是一个考察回溯法的题目。

首先，我们来分析一下这个问题的难点在哪里。一般的回溯法题目对于下一个转移状态是很明确告知的，比如常见的地图的4或者8个方向，但是这个题目的回溯转移是需要我们简单设计一下，那就是把两个连续的字符串能够生成的所有第三个字符放到列表里，当做我们下一个前进的方向。如果把这个转移状态设计好了，我们就很容易写出代码了。

我们在每层字符串作为底座的基础上，向上面建立新的一层。所以是个递归过程。建立的方式是通过允许的组合，这个组合是我们可以通过下面的这两块砖来获得上面可以累加什么砖的方式。

所以，用curr表示当前层，用above表示上层。当curr大小为2，above为1，那么金字塔完成。如果curr = above + 1，说明上面这层已经弄好了，下面使用above来作为当前层，继续递归。

如果上面两个都不满足，说明需要继续堆积above，做的方式是在应该继续堆积的位置上，找出能堆积哪些字符，并把这个字符堆积上去，做递归。

我犯了一个错误，是使用的map保存的是键值对，但是对于重复出现的情况就被替换掉了。因此使用list才行，代表了这两块砖上面允许堆积的砖。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82469175
版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        m = collections.defaultdict(list)
        for triples in allowed:
            m[triples[:2]].append(triples[-1])
        return self.helper(bottom, "", m)

    def helper(self, curr, above, m):
        if len(curr) == 2 and len(above) == 1:
            return True
        if len(above) == len(curr) - 1:
            return self.helper(above, "", m)
        pos = len(above)
        base = curr[pos : pos+2]
        if base in m:
            for ch in m[base]:
                if self.helper(curr, above + ch, m):
                    return True
        return False

