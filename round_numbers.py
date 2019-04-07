When you book on airbnb the total price is:
Total price = base price + service fee + cleaning fee + ...
input : array of decimals ~ X
output : array of int ~ Y
But they need to satisfy the condition:
sum(Y) = round(sum(x))
minmize (|y1-x1| + |y2-x2| + ... + |yn-xn|)
Example1:
input = 30.3, 2.4, 3.5
output = 30 2 4
Example2:
input = 30.9, 2.4, 3.9
output = 31 2 4
airbnb面试题汇总
先将所有floor(x)加起来统计出如果所有都floor的话还差多少，按照ceil以后需要加的价格排序，贪心取最小的补齐即可。


import math
import sys

class Solution(object):
    def roundNum(self, input):
        output = list(map(lambda x: math.floor(x), input))
        remain = int(round(sum(input)) - sum(output))
        it = sorted(enumerate(input), key=lambda x: x[1] - math.floor(x[1]))
        # print(it)
        # sys.exit(1)
        for _ in range(remain):
            t = it.pop()[0]
            output[t] += 1
        return output

s = Solution()
output = s.roundNum([30.3, 2.4, 3.5])
print(output)
