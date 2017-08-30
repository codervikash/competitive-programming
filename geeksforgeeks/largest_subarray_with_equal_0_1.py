#!/usr/bin/python

def get_largst_subarray(arr):
    l = len(arr)
    sum_left = [-1] * l
    sum_left[0] = 1 if arr[0] == 1 else -1
    max_size = - 1
    hash_table = 
    hash_table[0] = sum_left[0]
    start_index = 0
    for i in xrange(1, l):
        sum_left[i] = sum_left[i - 1] + (1 if arr[i] == 1 else -1)
        
        if sum_left[i] == 0:
            max_size = i
            start_index = 0
    print sum_left, max_size, start_index
    
    for j in xrange(stop):
        if each in su


arr = [1, 0, 0, 1, 0, 1, 1]
print('Largest subarray with equal number of 0 and 1: ' + str(get_largst_subarray(arr)))