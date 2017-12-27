"""
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
"""

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_parent(self, i):
        return (i  - 1)/2

    def get_left_child(self, i):
        return 2*i + 1

    def get_right_child(self, i):
        return 2*i + 2

    def heapify(self, index):
        minimum = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)

        if left < self.size and self.heap[left].val < self.heap[minimum].val:
            minimum = left

        if right < self.size and self.heap[right].val < self.heap[minimum].val:
            minimum = right

        if minimum != index:
            self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
            self.heapify(minimum)

        return

    def add_key(self, key):
        self.size += 1
        self.heap.append(key)
        i = self.size - 1
        while i != 0 and self.heap[self.get_parent(i)].val > self.heap[i].val:
            self.heap[i], self.heap[self.get_parent(i)] = self.heap[self.get_parent(i)], self.heap[i]
            i = self.get_parent(i)

    def extract_min(self):
        minimum = self.heap[0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        del(self.heap[self.size - 1])
        self.size -= 1
        self.heapify(0)

        return minimum

    def build_heap(self, ls):
        self.heap = ls
        print self.heap
        self.size = len(ls)
        for i in xrange(self.size - 1, - 1, - 1):
            self.heapify(i)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = Heap()
        l = len(A)
        head = ListNode(0)
        for i in xrange(l):
            heap.add_key(A[i])

        previous_node = head
        while heap.size > 0:
            current_node = heap.extract_min()
            previous_node.next = current_node
            previous_node = previous_node.next
            if current_node.next:
                heap.add_key(current_node.next)

        return head.next
