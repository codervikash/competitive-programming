#!/usr/bin/python

"""
https://www.hackerrank.com/contests/w33/challenges/transform-to-palindrome
"""

import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self._graph = defaultdict(set)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        q = deque([node1])
        visited = set([node1])
        if node1 == node2:
            return True
        while len(q):
            node = q.popleft()
            if node2 not in self._graph[node]:
                for each in self._graph[node]:
                    if each not in visited:
                        visited.add(each)
                        if each == node2:
                            return True
                        else:
                            q.append(each)
            else:
                return True

        return False

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def palindrome(str):
    n = len(str)
    L = [[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        L[i][i] = 1

    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if (str[i] == str[j] or g.is_connected(str[i], str[j])) and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j] or g.is_connected(str[i], str[j]):
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1]


n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
g = Graph()
for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    g.add(int(x),int(y))

arr = map(int, raw_input().strip().split(' '))


print palindrome(arr)