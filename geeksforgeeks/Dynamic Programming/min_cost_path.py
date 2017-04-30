#!/usr/bin/python

def min_cost(cost, m, n):
	if m < 0 or n < 0:
		return 10000 # some max value
	if m == 0 and n == 0:
		return cost[m][n]

	return cost[m][n] + min(
		min_cost(cost, m -  1, n - 1),
		min_cost(cost, m, n - 1),
		min_cost(cost, m - 1, n)
	)
	
	
def min_cost_dp(cost, m, n):
	if tc[m][n]:
		return tc[m][n]

	if m < 0 or n < 0:
		tc[m][n] = 10000 # some max value
	elif m == 0 or n == 0:
		tc[m][n] = cost[m][n]
	else:
		tc[m][n] = cost[m][n] + min(
			min_cost(cost, m -  1, n - 1),
			min_cost(cost, m, n - 1),
			min_cost(cost, m - 1, n)
		)

	return tc[m][n]
	
def min_cost_bottomup(cost, m, n):
	tc[0][0] = cost[0][0]
	
	for i in xrange(1, m + 1):
		tc[i][0] = tc[i - 1][0] + cost[i][0]

	for j in xrange(1, n + 1):
		tc[0][j] = tc[0][j - 1] + cost[0][j]
		
	for i in xrange(1, m + 1):
		for j in xrange(1, n + 1):
			tc[i][j] = cost[i][j] + min(
				tc[i - 1][j],
				tc[i][j - 1],
				tc[i - 1][j - 1]
			)
		
	return tc[m][n]
	

cost = [[1, 2, 3],
	[4, 8, 2],
	[1, 5, 3]]
tc = [[0 for x in range(3)] for x in range(3)]
print('Minimum cost: \n')
print(min_cost(cost, 2, 2))
print(min_cost_dp(cost, 2, 2))
print(min_cost_bottomup(cost, 2, 2))