# -*- coding: utf-8 -*-
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy_head = ListNode(0)        
        n = dummy_head
        ncarry = 0
        while l1 is not None and l2 is not None:
            (ncarry, nsum) = divmod(l1.val + l2.val + ncarry, 10)            
            n.next = ListNode(nsum)
            n = n.next
            l1 = l1.next
            l2 = l2.next
            
        while l1 is not None:
            (ncarry, nsum) = divmod(l1.val + ncarry, 10)
            n.next = ListNode(nsum)
            n = n.next
            l1 = l1.next
        
        while l2 is not None:
            (ncarry, nsum) = divmod(l2.val + ncarry, 10)
            n.next = ListNode(nsum)
            n = n.next
            l2 = l2.next
            
        if ncarry:
            n.next = ListNode(ncarry)
            
        return dummy_head.next
                    
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        
        dummy_head = ListNode(0)
        n = dummy_head
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            n.next = ListNode(carry % 10)
            n = n.next
            carry //= 10
        
        if carry:
            n.next = ListNode(carry)
            
        return dummy_head.next