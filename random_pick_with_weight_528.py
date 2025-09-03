https://blog.csdn.net/fuxuemingzhu/article/details/81807215

import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i-1] + w[i]

    def pickIndex(self) -> int:
        total = self.preSum[-1]
        rand = random.randint(1, total) # random int from [1, total]
        ind = bisect.bisect_left(self.preSum, rand)
        return ind