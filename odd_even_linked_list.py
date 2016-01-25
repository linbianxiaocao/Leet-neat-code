# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# 
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # this is my attempt
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        newHead = head        
        evenHead = head.next
        evenTail = ListNode(0)
        while True:
            evenTail.next = head.next
            evenTail = evenTail.next
            if evenTail is None or evenTail.next is None:
                head.next = evenHead
                return newHead
            else:
                head.next = head.next.next 
                head = head.next
    
    # a more elegant solution
    def oddEvenList2(self, head):
        if head is None: return head
        odd = oddHead = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead
