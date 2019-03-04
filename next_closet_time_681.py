# http://bookshadow.com/weblog/2017/09/24/leetcode-next-closest-time/

# 这个解法最牛（简洁，明白）

解题思路：
将time的数字取出并排序，记为stime，令X = stime[0]

从time的低位向高位枚举，将stime中恰好大于当前值的值进行替换，并将其后的所有值替换为X

若不存在这样的替换，则返回XX:XX

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time[:2] + time[3:]
        isValid = lambda t: int(t[:2]) < 24 and int(t[2:]) < 60
        stime = sorted(time)
        for x in (3, 2, 1, 0):
            for y in stime:
                if y <= time[x]: continue
                ntime = time[:x] + y + (stime[0] * (3 - x))
                if isValid(ntime): return ntime[:2] + ':' + ntime[2:]
        return stime[0] * 2 + ':' + stime[0] * 2

也可以参考花花酱解法：https://zxi.mytechroad.com/blog/simulation/leetcode-681-next-closest-time/
