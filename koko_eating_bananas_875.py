class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # ref: huahua binary search https://www.youtube.com/watch?v=v57lNF2mb_s
        l = 1
        r = max(piles) + 1
        while l < r:
            m = l + (r-l) // 2
            h = 0
            for p in piles:
                h += (p-1) // m + 1
            if h <= H:
                r = m
            else:
                l = m + 1
        return l