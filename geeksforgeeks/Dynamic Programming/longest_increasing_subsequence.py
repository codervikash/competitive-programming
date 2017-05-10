#!/usr/bin/python

# Reccursive solution
def lis_recursive(arr, n):
	if n == 1:
		return 1
	
	current_lis_length = 1

	for i in xrange(n):
		subproblem_lis_length = lis_recursive(arr, i)
		
		if arr[i - 1] < arr[n - 1] and current_lis_length < (1 + subproblem_lis_length):
			current_lis_length = 1 + subproblem_lis_length
		elif current_lis_length < subproblem_lis_length:
			current_lis_length = subproblem_lis_length

	return current_lis_length
	
	
# Dynamic programming approach
def lis_dp(arr):
	size = len(arr)
	lis = [1] * size
	
	for i in xrange(1, size):
		for j in xrange(i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
#			elif lis[i] < lis[j]:
#				lis[i] = lis[j]
				
#	return lis[size - 1]
	return max(lis)

liss = [0] * 1000

def lis_dp_recursive(arr, n):
	if n == 1:
		return 1

	liss[n] = 1
	for i in xrange(n):
		if not liss[i]:
			liss[i] = lis_dp_recursive(arr, i)
			
		if arr[i - 1] < arr[n - 1] and liss[n] < (1 + liss[i]):
			liss[n] = 1 + liss[i]
		elif liss[n] < liss[i]:
			liss[n] = liss[i]
			
	return liss[n]
			
		
	
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 100]
print('Longest Increasing Subsequence(LIS) for [10, 22, 9, 33, 21, 50, 41, 60, 80] is')
print(lis_recursive(arr, len(arr)))
print (lis_dp(arr))
print(lis_dp_recursive(arr, len(arr)))