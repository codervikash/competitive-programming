#!/usr/bin/python

def coin_change(arr, m, n):
	if m <= 0 and n > 0: 
		return 0

	if n == 0:
		return 1
		
	if n < 0:
		return 0

	return coin_change(arr, m - 1, n ) + coin_change(arr, m, n-arr[m-1] )
	
arr = [1, 2, 3]
m = len(arr)
n = 4
print(coin_change(arr, m, n)) 