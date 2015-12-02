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
        