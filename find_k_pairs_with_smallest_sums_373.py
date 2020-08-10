# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        heapq.heappush(queue, [nums1[0]+nums2[0], 0, 0])
        
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            
            if j+1 < len(nums2):
                heapq.heappush(queue, [nums1[i]+nums2[j+1], i, j+1])
            
            if j == 0: # this is optimization
                if i+1 < len(nums1):
                    heapq.heappush(queue, [nums1[i+1]+nums2[j], i+1, j])        
        return pairs