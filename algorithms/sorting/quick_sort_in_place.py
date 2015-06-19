# Problem Statement
#
# The previous version of Quicksort was easy to understand, but it was not optimal. It required copying the numbers into other arrays, which takes up space and time. To make things faster, one can create an "in-place" version of Quicksort, where the numbers are all sorted within the array itself.
#

def quick(A, p , r):
	if p < r:
		q = partition(A, p , r)
		quick(A, p, q - 1)
		quick(A, q + 1, r)

def partition(A, p , r):
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]

	print ' '.join(map(str,A))
	return i + 1

x = int(raw_input())
a = [int (i) for i in raw_input().strip().split()]

quick(a, 0, x-1)
