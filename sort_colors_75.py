https://www.cnblogs.com/zuoyuan/p/3775832.html

解题思路：这道题不允许使用排序库函数。那么最直观的解法是：遍历两遍数组，第一遍对0，1，2计数，第二遍对数组进行赋值，这样是可以ac的。但题目的要求是只使用常数空间，而且只能遍历一遍。那么思路就比较巧妙了。设置两个头尾指针，头指针p0指向的位置是0该放置的位置，尾指针p2指向的位置是2该放置的位置。i用来遍历整个数组，碰到0把它和p0指向的数交换，碰到2把它和p2指向的数交换，碰到1继续向后遍历。有点类似快速排序的分割数组这一步。
代码：


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    # @should learn another algorithm
    def sortColors(self, A):
        if A == []: return
        p0 = 0; p2 = len(A) - 1; i = 0
        while i <= p2:
            if A[i] == 2:
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            elif A[i] == 0:
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
                i += 1
            else:
                i += 1
