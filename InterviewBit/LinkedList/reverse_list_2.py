"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        current_node = A
        new_head = ListNode(0)
        new_head.next = A
        next_node = None
        prev_node = None
        prev_prev_node = None

        for i in xrange(m - 1):
            prev_prev_node = current_node
            current_node = current_node.next

        start_node = current_node
        while m <= n:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            m += 1
        if prev_prev_node:
            prev_prev_node.next = prev_node

        start_node.next = current_node

        return new_head.next

        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
