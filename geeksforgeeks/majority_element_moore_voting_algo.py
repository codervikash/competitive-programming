#!/usr/bin/python

"""
Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:

       I/P : 3 3 4 2 4 4 2 4 4
       O/P : 4 

       I/P : 3 3 4 2 4 4 2 4
       O/P : NONE

Using Moore Voting Algorithm:

1. Get an element occurring most of the time in the array. This phase will make sure that if there is a majority element then it will return that only.
2. Check if the element obtained from above step is majority element.
"""

def majority_element(arr):
    l = len(arr)
    maj_index = 0
    count = 0

    for i in xrange(l):
        if arr[i] == arr[maj_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    count = 0
    for i in xrange(l):
        if arr[i] == arr[maj_index]:
            count += 1

    if count == l/2:
        return arr[maj_index]


arr = [1, 3, 3, 1, 2]
print 'majority element in array: ' + str(majority_element(arr))

arr = [1, 3, 3, 1, 2, 3]
print 'majority element in array: ' + str(majority_element(arr))