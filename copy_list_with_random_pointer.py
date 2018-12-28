# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# https://siddontang.gitbooks.io/leetcode-solution/content/linked_list/copy_list_with_random_pointer.html

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None:
            return None

        dict = {}
        head_copy = RandomListNode(head.label)
        node = head
        node_copy = head_copy
        dict[head] = head_copy

        while node.next:
            nextNode = node.next
            nextNode_copy = RandomListNode(nextNode.label)
            node_copy.next = nextNode_copy
            dict[nextNode] = nextNode_copy
            node = node.next
            node_copy = node_copy.next

        node = head
        node_copy = dict[node]
        while node:
            node_copy = dict[node]
            node_copy.random = dict[node.random]
            node = node.next

        return head_copy







