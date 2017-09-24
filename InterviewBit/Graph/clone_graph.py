"""

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

from collections import deque

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        m = {}
        q = deque()
        q.append(node)
        clone_node = UndirectedGraphNode(node.label)
        m[node] = clone_node

        while q:
            temp = q.popleft()
            neighbors = temp.neighbors
            for neighbor in neighbors:
                if neighbor not in m:
                    neighbor_clone = UndirectedGraphNode(neighbor.label)
                    m[neighbor] = neighbor_clone
                    q.append(neighbor)

                m[temp].neighbors.append(m[neighbor])


        return m[node]
