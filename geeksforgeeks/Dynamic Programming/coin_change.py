#!/usr/bin/python

def coin_change(arr, m, n):
	if m <= 0 and n > 0: 
		return 0

	if n == 0:
		return 1
		
	if n < 0:
		return 0

	return coin_change(arr, m - 1, n ) + coin_change(arr, m, n-arr[m-1] )

def coin_change_recursive(arr, m, n):
	change = [0]
	
	for i in xrange(n + 1):
		for j in xrange(m):
			
			


arr = [1, 2, 3]
m = len(arr)
n = 4
print(coin_change(arr, m, n)) 