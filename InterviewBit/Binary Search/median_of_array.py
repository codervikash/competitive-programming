"""
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
 NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
"""

class Solution:
    def median2(self, x, y):
        return (x + y )/ 2.0

    def median3(self, a, b, c):
        return ( a + b + c - max(a, max(b, c)) - min (a, min(b, c)) )

    def median4(self, a, b, c, d):
        max1 = max( a, max( b, max( c, d )))
        min1 = min( a, min( b, min( c, d )))
        return ( a + b + c + d - max1 - min1 ) / 2.0

    def median(self, A, l):
        if l == 0:
            return -1
        elif l % 2 == 0:
            return (A[l/2] + A[l/2 - 1]) / 2.0
        else:
            return A[l/2]

    def median_util(self, A, l1, B, l2):
        if l1 == 0:
            return self.median(B, l2)

        if l1 == 1:
            if l2 == 1:
                return self.median2(A[0], B[0])

            if l2 & 1:
                return self.median2( B[l2/2], self.median3(A[0], B[l2/2 - 1], B[l2/2 + 1]) )

            return self.median3( B[l2/2], B[l2/2 - 1], A[0] )

        elif l1 == 2:
            if l2 == 2:
                return self.median4(A[0], A[1], B[0], B[1])

            if l2 & 1:
                return self.median3( B[l2/2], max(A[0], B[l2/2 - 1]), min(A[1], B[l2/2]))

            return self.median4( B[l2/2], B[l2/2 - 1], max( A[0], B[l2/2 - 1] ), min( A[1], B[l2/2] ))

        idxA = ( l1 - 1 ) / 2;
        idxB = ( l2 - 1 ) / 2;

        if A[idxA] <= B[idxB]:
            return self.median_util(A[idxA:], l1/2 + 1, B, l2 - idxA );

        return self.median_util(A, l1/2 + 1, B[idxB:], l2 - idxA );


    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        l1 = len(A)
        l2 = len(B)
        if l1 < l2:
            median = self.median_util(A, l1, B, l2)
        else:
            median = self.median_util(B, l2, A, l1)

        return median
