# Problem Statement

# Given a list of N integers, your task is to select K integers from the list such that its unfairness is minimized.

# if (x1,x2,x3,…,xk) are K numbers selected from the list N, the unfairness is defined as

# max(x1,x2,…,xk)−min(x1,x2,…,xk)
# where max denotes the largest integer among the elements of K, and min denotes the smallest integer among the elements of K.

# Input Format
# The first line contains an integer N.
# The second line contains an integer K.
# N lines follow. Each line contains an integer that belongs to the list N.

# Note: Integers in the list N may not be unique.

# Output Format
# An integer that denotes the minimum possible value of unfairness.

# Constraints
# 2≤N≤105
# 2≤K≤N
# 0≤integer in N ≤109

n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
temp = candies[1+k-1] - candies[1]
for i in range(0,n-k+1):
  diff = candies[i + k-1] - candies[i]
  if diff < temp:
    temp = diff
  i +=1

print temp