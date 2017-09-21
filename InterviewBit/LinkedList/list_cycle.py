"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        fast_ptr = A
        slow_ptr = A

        while fast_ptr and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

            if fast_ptr == slow_ptr:
                ptr1 = slow_ptr
                ptr2 = slow_ptr

                k = 1
                while(ptr1.next != ptr2):
                    ptr1 = ptr1.next
                    k += 1

                ptr1 = A

                ptr2 = A
                for i in range(k):
                    ptr2 = ptr2.next

                while(ptr2 != ptr1):
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next

                ptr2 = ptr2.next
                while(ptr2.next != ptr1):
                    ptr2 = ptr2.next

                return ptr2.next

        return
