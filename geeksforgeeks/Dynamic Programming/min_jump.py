#!/usr/bin/python

max_value = 20
jump = [max_value]*10

def min_jump_dp_recursive(arr, l, n):
	if l == 0 or arr[0] == 0:
		return max_value

	jump[0] = 0
	for i in xrange(l):
	
def min_jump(arr):
	l = len(arr)
	jump = [max_value for x in xrange(l)] 
	
	if l == 0 or arr[0] == 0:
		return max_value
		
	jump[0] = 0
	for i in xrange(l):
		for j in xrange(i):

			if i <= j + arr[j] and jump[j] != max_value:
				jump[i] = min(jump[i], jump[j] + 1)
				break

	return jump[l - 1]
		
	


arr = [1, 3, 6, 1, 0, 9]
print('MIn jump is')
#print(lis_recursive(arr, len(arr)))
print (min_jump(arr))
print(min_jump_dp_recursive(arr, 0, len(arr)))