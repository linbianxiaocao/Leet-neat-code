# https://leetcode.com/problems/exam-room/
https://blog.csdn.net/fuxuemingzhu/article/details/83141523

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N, self.L = N, []

    def seat(self):
        """
        :rtype: int
        """
        N, L = self.N, self.L
        res = 0
        if not L:
            res = 0
        else:
            d = L[0]
            for i in range(len(L)-1):
                a, b = L[i], L[i+1]
                if (b-a) / 2 > d:
                    d = (b-a) / 2
                    res = (b+a) / 2
            if N-1-L[-1] > d:
                res = N-1

        # binary insert res
        bisect.insort(L, res)

        return res


    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


http://bookshadow.com/weblog/2018/06/17/leetcode-exam-room/
解题思路：
TreeSet

将每两个座位之间的位置视为“区间”

利用一个TreeSet维护这样的区间，记为pq

用另一个TreeSet维护当前被占用的座位标号，记为seats。

对于leave操作，seats可以用O(log n)的代价找到某座位相邻的座位。并将两个区间合二为一。

对于seat操作，可以通过pq获取当前的最大区间，将区间一分为二。
