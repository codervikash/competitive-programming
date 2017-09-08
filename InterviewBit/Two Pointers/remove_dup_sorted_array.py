"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1

        return last + 1
