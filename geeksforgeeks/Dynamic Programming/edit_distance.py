#!/usr/bin/python

def edit_distance(x, y, n, m):
	if m == 0:
		return n

	if n == 0:
		return m
		
	if x[n - 1] == y[m - 1]:
		return edit_distance(x, y, n - 1, m - 1)

	return 1 + min(
		edit_distance(x, y, n - 1, m),
		edit_distance(x, y, n, m - 1),
		edit_distance(x, y, n - 1, m - 1)
	)
	
def edit_distance_dp_recursive(x, y, n, m):
	if edit_arr[n][m]:
		return edit_arr[m][n]
	if m == 0:
		edit_arr[n][m] = n

	if n == 0:
		edit_arr[n][m] = m

	if x[n - 1] == y[m - 1]:
		edit_arr[n][m] = edit_distance(x, y, n - 1, m - 1)
	else:
		edit_arr[n][m] = 1 + min(
			edit_distance(x, y, n - 1, m),
			edit_distance(x, y, n, m - 1),
			edit_distance(x, y, n - 1, m - 1)
		)
	
	return edit_arr[n][m]
	
def edit_distance_dp_topdown(x, y, n, m):	
	for i in xrange(1, n):
		for j in xrange(1, m):
			if i == 0:
				edit_arr[i][j] = j

			if j == 0:
				edit_arr[i][j] = i

			if x[i] == y[j]:
				edit_arr[i][j] = edit_arr[i - 1][j - 1]
			else:
				edit_arr[i][j] = 1 + min(
					edit_distance(x, y, i - 1, j),
					edit_distance(x, y, i, j - 1),
					edit_distance(x, y, i - 1, j - 1)
				)
	return edit_arr[n][m]
			
	
str1 = "sunday"
str2 = "saturday"
edit_arr = [[None for i in xrange(len(str2) + 1)] for j in xrange(len(str1) + 1)]
print edit_distance(str1, str2, len(str1), len(str2))
print edit_distance_dp_recursive(str1, str2, len(str1), len(str2))
print edit_distance_dp_topdown(str1, str2, len(str1), len(str2))