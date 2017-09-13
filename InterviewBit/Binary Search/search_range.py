"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
"""

class Solution:
    def first(self, A, B):
        occurance = -1
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end )/2
            if A[mid] == B and (mid == start or  A[mid - 1] < B):
                occurance = mid
                return occurance

            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1

        return occurance

    def last(self, A, B):
        occurance = -1
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end )/2
            if A[mid] == B and (mid == end or A[mid + 1] > B):
                occurance = mid
                return occurance

            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1

        return occurance


    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        first = self.first(A, B)
        second = self.last(A, B)

        return [first, second]
