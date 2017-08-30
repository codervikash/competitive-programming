"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands

Complexity: O(row x col)
"""

class Graph:
    def __init__(self, graph, row, col):
        self._graph = graph
        self._row = row
        self._col = col

    def is_safe(self, row, col):

        return (row >= 0 and row <= self._row and
                row >= 0 and row < self._col and
                not self.visited[row][col] and self._graph[row][col])

    def dfs(self, i, j, visited):
        row_nbr = [-1, -1 -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, 1, -1, 0, -1, 1]

        visited[i][j] = True

        for k in xrange(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k]), visited):
                self.dfs(i + row_nbr[k], j + col_nbr[k], visited)

        return

    def count_islands(self):
        visited = [False for i in xrange(self._col) False for j in xrange(self._row)]
        count = 0

        for i in xrange(self._row):
            for j in xrange(self._col):
                if self._graph[i][j] == 0 and visited[i][j] == False:
                    self.dfs(i, j, visited)
                    count += 1


        return count


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]


row = len(graph)
col = len(graph[0])

g= Graph(row, col, graph)

print "Number of islands is :"
print g.countIslands()

