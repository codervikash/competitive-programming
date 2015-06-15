# Problem Statement

# Given an array A={a1,a2,…,aN} of N elements, find the maximum possible sum of a

# Contiguous subarray
# Non-contiguous (not necessarily contiguous) subarray.
# Empty subarrays/subsequences should not be considered.

# Input Format

# First line of the input has an integer T. T cases follow.
# Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

# Constraints:

# 1≤T≤10
# 1≤N≤105
# −104≤ai≤104
# The subarray and subsequences you consider should have at least one element.

# Output Format

# Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

def max_subarray(a):
  sum_cont = 0
  sum_noncont = 0
  current_sum = 0
  large = -999
  count = 0


  for i in range(len(a)):
    if a[i] < 0:
      count += 1
      if a[i] > large:
        large = a[i]
    if a[i] >= 0 :
      sum_noncont += a[i]
    val = current_sum + a[i]
    if val > 0:
      current_sum = val

    else:
      current_sum = 0

    if current_sum > sum_cont:
      sum_cont = current_sum
    elif count == len(a):
      sum_cont = large
      sum_noncont = large


  print sum_cont, sum_noncont


x = int(raw_input())
for i in range(x):
  y = int(raw_input())
  z = map(int, raw_input().strip().split())
  max_subarray(z)
