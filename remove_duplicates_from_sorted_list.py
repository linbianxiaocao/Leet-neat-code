""""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
            
        node = head
        while node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
            
        return head
		
		
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        c_node = head
        n_node = c_node.next
        
        while True:            
            if not n_node:
                c_node.next = None
                return head
            if n_node.val == c_node.val:
                n_node = n_node.next
                continue
            c_node.next = n_node
            c_node = n_node
            n_node = n_node.next
            
        return head		