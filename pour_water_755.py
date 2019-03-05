http://www.cnblogs.com/grandyang/p/8460541.html

class Solution:
  def pourWater(self, heights, V, K):
	for i in range(0, V):
		l, r = K, K

		while l > 0 and heights[l] >= heights[l-1]:
			l -= 1
		while l < K and heights[l] == heights[l+1]:
			l += 1
		while r < n-1 and heights[r] >= heights[r+1]:
			r += 1
		while r > K and heights[r] == heights[r-1]:
			r -= 1
		if heights[l] < heights[K]:
			heights[l] += 1
		else:
			heights[r] += 1

	return heights
