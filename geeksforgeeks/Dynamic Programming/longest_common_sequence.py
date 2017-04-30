#!/usr/bin/python

def lcs_recursive_naive(x, y, n, m):
	if n == 0 or m == 0:
		return 0

	elif x[n - 1] == y[m - 1]:
		return 1 + lcs_recursive_naive(x, y, n - 1, m - 1)
	else:
		return max(
			lcs_recursive_naive(x, y, n - 1, m),
			lcs_recursive_naive(x, y, n, m - 1)
		)


def lcs_dp_recursive(x, y, n, m):
	if lcs[n][m] != 0:
		return lcs[n][m]
	if n == 0 or m == 0:
		lcs[n][m] = 0
	elif x[n - 1] == y[m - 1]:
		lcs[n][m] = 1 + lcs_dp_recursive(x, y, n - 1, m - 1)
	else:
		lcs[n][m] = max(
			lcs_dp_recursive(x, y, n - 1, m),
			lcs_dp_recursive(x, y, n, m - 1)
		)
		
	return lcs[n][m]

def lcs_dp_tabulated(x, y, n, m):
	for i in range(n):
		for j in range(m):
			if i == 0 or j == 0:
				lcs[i][j] = 0
			elif x[i] == y[j]:
				lcs[i][j] = lcs[i-1][j-1] + 1
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

	return lcs[n][m]
				
				
	

X = "AGGTAB"
Y = "GXTXAYB"
lcs = [[0 for x in xrange(len(Y) + 1)] for y in xrange(len(X) + 1)]

print "\nLength of LCS is (recursive naive): ", lcs_recursive_naive(X , Y, len(X), len(Y))

print "\nLength of LCS is (recursive DP): ", lcs_dp_recursive(X , Y, len(X), len(Y))

print "\nLength of LCS is (bottom up DP): ", lcs_dp_tabulated(X , Y, len(X), len(Y))