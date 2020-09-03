class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # beautiful solution: https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/780926/Python-Simple-presum-%2B-dict-greedy-solution-with-explaination-O(N)
        
        presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        
        seen = {0: 0}
        ans = 0
        for i in range(1, len(nums) + 1):
            curr = presum[i]
            prev = curr - target
            if prev in seen:
                ans += 1
                seen = {}
            seen[curr] = i
        
        return ans