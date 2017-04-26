#!/usr/bin/python

"""
Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[]. The functions should put all 0s first, then all 1s and all 2s in last.

Example
Input = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
Output = {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
"""

def sort_occurance(arr):
	size = len(arr)
	mid = 0
	i = 0
	j = size -1
	while mid <= j:
		if arr[mid] == 0:
			arr[mid], arr[i] = arr[i], arr[mid]
			i += 1
			mid += 1
			
		elif arr[mid] == 1:
			mid += 1
			
		elif arr[mid] == 2:
			arr[mid], arr[j] = arr[j], arr[mid]
			j -= 1
			
	return arr
	
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort_occurance(arr))
			
			
		
	