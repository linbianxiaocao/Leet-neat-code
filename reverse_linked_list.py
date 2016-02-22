# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if head is None:
            return None
            
        p = None
        c = head                
        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n
            
        return p
        
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if head is None or head.next is None:
            return head
        
        n = head.next
        head.next = None
        new_head = self.reverseList(n)
        n.next = head
        
        return new_head

class Solution3(object):
    def reverseList(self, head):
	# same algorithm as reverse() function in reverse_linked_list.py
        if head == None:
            return None
	dummy = ListNode(0)
	dummy.next = head
	while head.next != None:
	    tmp = head.next
	    head.next = tmp.next
	    tmp.next = dummy.next
	    dummy.next = tmp
	return dummy.next
