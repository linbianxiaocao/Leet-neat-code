# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container.

# tip: keep two indies i and j, and start on both ends of the array
# compare this problem with "largest_rectangle_area"
class Solution(object):
    def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
        maxA = 0
        i = 0
        j = len(height) - 1
    
        while i < j:
            curArea = (j-i) * min(height[i], height[j])
            maxA = max(curArea, maxA)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
    
        return maxA
