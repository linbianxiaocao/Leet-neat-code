# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer

    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        f1 = 1
        f2 = 2
        f = 0
        for i in range(n-2):
            f = f1 + f2
            f1 = f2
            f2 = f
            
        return f


    def climbStairs(self, n):
	if n == 1 or n == 2:
	    return n
	dn = [1, 2]
	for i in range(2, n):
	   ns = dn[i-1] + dn[i-2]
	   dn.append(ns)
        return dn[-1] 
