# You are given a square map of size n×nn×n. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).
#
# You need to find all the cavities on the map and depict them with the uppercase character X.
#
# Input Format
#
# The first line contains an integer, nn, denoting the size of the map. Each of the following nn lines contains nn positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.
#
# Constraints
# 1≤n≤1001≤n≤100
# Output Format
#
# Output nn lines, denoting the resulting map. Each cavity should be replaced with character X.
#
# Sample Input
#
# 4
# 1112
# 1912
# 1892
# 1234
# Sample Output
#
# 1112
# 1X12
# 18X2
# 1234


n = int(raw_input().strip())
grid = a = []
for grid_i in xrange(n):
    grid_t = map(str, raw_input().strip())
    grid.append(grid_t)
for i in xrange(1, n-1):
    for j in xrange(1, n-1):
        if grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
            if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j]:
                a[i][j] = 'X'

for i in range(n):
    print ''.join(a[i])
