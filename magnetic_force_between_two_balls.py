class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/Python-Binary-search-solution-with-explanation-and-similar-questions
        n = len(position)
        position.sort()
        
        # Define function count(d) that counts the number of balls can be placed in to baskets, under the condition that the minimum distance between any two balls is d
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans        
        
        l, r = 0, position[-1] - position[0] + 1
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) < m:  # return smallest mid such that this condition is true
                r = mid
            else:
                l = mid + 1
        return l-1        
        
        
        # tricky, attention, compare (this not work)
        l, r = 0, position[-1] - position[0] + 1
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) <= m:  # return smallest mid such that this condition is true
                r = mid
            else:
                l = mid + 1
        return l              