解题思路

第一个for循环，从第0个人开始，如果k是第0个人认识的第一个人，说明1到k-1这些人0不认识，所以排除了名人的可能。按照此规则进行下去，最后candidate停在某一个位置，这个位置后面一定也没有名人，因为有的话，candidate会update等于它
最后检查candidate对不对

作者：Jason_Yuan
链接：https://www.jianshu.com/p/dca466058b1c
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

note: 排除法

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if candidate != i and (knows(candidate, i) or knows(i, candidate)):
                return -1
        return candidate
