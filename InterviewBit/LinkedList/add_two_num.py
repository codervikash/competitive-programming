"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        dummy_node = ListNode(0)
        added_list = dummy_node
        carry = 0

        while A is not None or B is not None:
            a_data = A.val if A is not None else 0
            b_data = B.val if B is not None else 0

            s = a_data + b_data + carry
            carry = 1 if s >= 10 else 0
            s = s if s < 10 else s % 10

            added_list.next = ListNode(s)
            added_list = added_list.next

            A = A.next if A is not None else A
            B = B.next if B is not None else B

        if carry:
            added_list.next = ListNode(carry)

        return dummy_node.next
