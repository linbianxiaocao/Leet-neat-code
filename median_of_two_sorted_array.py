# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.findKth(nums1, nums2, (len1 + len2) // 2 + 1)
        else:
            return 0.5 * (self.findKth(nums1, nums2, (len1 + len2) // 2) \
            + self.findKth(nums1, nums2, (len1 + len2) // 2 + 1))


    def findKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.findKth(B, A, k)
        if lenA == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(k // 2, lenA)
        pb = k - pa
        if A[pa-1] < B[pb-1]:
            return self.findKth(A[pa:], B, k - pa)
        elif A[pa-1] > B[pb-1]:
            return self.findKth(A, B[pb:], k - pb)
        else:
            return A[pa-1]

-------------- cpp ---------------
class Solution {
public:
    // https://blog.csdn.net/yutianzuijin/article/details/11499917
    // also reference https://www.cnblogs.com/grandyang/p/4465932.html 解法二
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), total = m+n;

        if (total & 1)
	    // use nums1.data() to get pointer, instead of &nums1[0], because nums1 could be an empty vector
            return findKth(nums1.data(), m, nums2.data(), n, total/2+1);
        else
            return (findKth(nums1.data(), m, nums2.data(), n, total/2) +
                    findKth(nums1.data(), m, nums2.data(), n, total/2+1)) / 2.0;
    }

    int findKth(int a[], int m, int b[], int n, int k) {
        if (m > n) return findKth(b, n, a, m, k);
        if (m == 0) return b[k-1];
        if (k == 1) return min(a[0], b[0]);

        int pa = min(k/2, m), pb = k-pa;
        if (a[pa-1] < b[pb-1])
            return findKth(a+pa, m-pa, b, n, k-pa);
        else if (a[pa-1] > b[pb-1])
            return findKth(a, m, b+pb, n-pb, k-pb);
        else return a[pa-1];
    }
};
