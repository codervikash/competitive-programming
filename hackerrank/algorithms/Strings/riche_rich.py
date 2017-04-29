#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
number = raw_input().strip()

def riche(number, n,k):
	if n % 2 == 0:
		min = n/2
	else:
		min = (n-1)/2
	number = list(number)
	map = set()
	for i in xrange(n/2):
		if number[i] != number[n-i-1] and k >= 1:
			number[n-i-1] = number[i] = max(number[n-i-1], number[i])
			map.add(i)
			k -= 1
		elif number[i] != number[n-i-1] and k < 1:
			return -1

	for i in xrange(n/2):
		if k > 0 and number[i] != '9':
			if i in map and k > 0:
				number[i] = number[n-i-1] = '9'
				k -= 1
			elif k > 1:
				number[i] = number[n-i-1] = '9'
				k -= 2
				
	if n %2 != 0 and k > 0:
		number[((n -1)/2)] = '9'

	return ''. join(number)

print riche(number, n,k)
