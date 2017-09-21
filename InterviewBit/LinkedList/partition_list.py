"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        l_node = ListNode(0)
        r_node = ListNode(0)
        left_list = l_node
        right_list = r_node
        current_node = A

        while current_node is not None:
            if current_node.val < B:
                left_list.next = current_node
                left_list = left_list.next
            elif current_node.val >= B:
                right_list.next = current_node
                right_list = right_list.next

            current_node = current_node.next

        left_list.next = r_node.next
        right_list.next = None

        return l_node.next
