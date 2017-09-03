#!/usr/bin/python

"""
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
Example:

Example 1 : Consider the following 3 activities sorted by
by finish time.

     start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};

A person can perform at most two activities.
The maximum set of activities that can be executed is {0, 2} [ These are indexes in start[] and finish[] ]
"""

def activity_selection(start, finish):
    n = len(finish)

    for i in xrange(n):
        if start[i] < finish[i]:
            print start[i]
            i = j


# Driver program to test above function
start = [1 , 3 , 0 , 5 , 8 , 5]
finish = [2 , 4 , 6 , 7 , 9 , 9]

activity_selection(start , finish)