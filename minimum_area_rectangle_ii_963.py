# 有了思路就不难了

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        N = len(points)
        # (l^2, x#, y#) : [(0,1), (1,2)]
        d = collections.defaultdict(list)
        for i in range(N - 1):
            pi = points[i]
            for j in range(i + 1, N):
                pj = points[j]
                l = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
                x = (pi[0] + pj[0]) / 2.0
                y = (pi[1] + pj[1]) / 2.0
                d[(l, x, y)].append((i, j))
        res = float("inf")
        for l in d.values():
            M = len(l)
            for i in range(M - 1):
                p0, p2 = points[l[i][0]], points[l[i][1]]
                for j in range(i + 1, M):
                    p1, p3 = points[l[j][0]], points[l[j][1]]
                    d1 = math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)
                    d2 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                    area = d1 * d2
                    res = min(res, area)
        return 0 if res == float('inf') else res
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/85223775
版权声明：本文为博主原创文章，转载请附上博文链接！
