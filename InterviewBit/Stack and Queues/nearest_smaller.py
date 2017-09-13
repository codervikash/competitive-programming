"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
"""

class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        stack = [arr[0]]
        result = [-1]
        l = len(arr)
        for i in xrange(1, l):
            while stack and stack[len(stack) - 1] >= arr[i]:
                stack.pop()
            if stack:
                popped = stack.pop()
                stack.append(popped)
                stack.append(arr[i])
                result.append(popped)
            else:
                stack.append(arr[i])
                result.append(-1)

        return result
