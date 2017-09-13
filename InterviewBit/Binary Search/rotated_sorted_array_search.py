"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, arr, x):
        start = 0
        end = len(arr) - 1
        result = -1
        while start <= end:
            mid = (start + end )/2
            if arr[mid] == x:
                result = mid
                break
            if arr[start] < arr[mid]:
                if x < arr[mid] and x >= arr[start]:
                    end =  mid - 1
                    continue

                start = mid + 1
                continue
            else:
                if  x > arr[mid]:
                    start =  mid + 1
                    continue

                end = mid - 1
                continue

        return result
