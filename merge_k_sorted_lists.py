# 面经：cruise automation, priority queue

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import sys


class Solution(object):
    # my own solution1: time limit exceeded
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        idx, smallest = -1, sys.maxsize
        for i in range(len(lists)):
            if lists[i] and lists[i].val < smallest:
                idx, smallest = i, lists[i].val

        if idx == -1:
            return None

        head = lists[idx]

        lists[idx] = lists[idx].next
        head.next = self.mergeKLists(lists)

        return head

    # my own solution2: use a min heap
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        import heapq
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))

        dummyhead = ListNode(0)
        cnode = dummyhead
        while len(h) != 0:
            (val, idx) = heapq.heappop(h)
            cnode.next = lists[idx]
            cnode = cnode.next

            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(h, (lists[idx].val, idx))

        return dummyhead.next
