# http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
# http://ronixy.com/2015/03/28/[LeetCode]-Container-With-Most-Water-Largest-Rectangle-in-Histogram/
# compare this problem with "container_with_most_water.py"
# A good example:
#    heights = [6, 2, 5, 4, 5, 1, 6]
#    maxArea = 12
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        maxArea = 0
        heights.append(0)

        while i < len(heights):
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if len(stack) != 0:
                    maxArea = max(heights[t] * (i - stack[-1] - 1), maxArea)
                else:
                    maxArea = max(heights[t] * i, maxArea)
                        
        return maxArea
        
