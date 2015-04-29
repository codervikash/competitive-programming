# You are given a tree (a simple connected graph with no cycles). You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest should contain an even number of vertices.

# To accomplish this, you will remove some edges from the tree. Find out the number of removed edges.

# Input Format
# The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges.
# The next M lines contain two integers ui and vi which specifies an edge of the tree. (1-based index)

# Output Format
# Print the answer, a single integer.

N, M = map(int, raw_input().split())
edges = []
for x in xrange(M):
    u, v = map(int, raw_input().split())
    edges.append([u, v])


info = []

def findChildren(n):
    children = []
    for x in xrange(M):
        if edges[x][1] == n:
            children.append(edges[x][0])
            childN = findChildren(edges[x][0])
            for child in childN:
                children.append(child)
    return children
tree = []
def generateTree():
    global tree
    for x in xrange(N):
    tree.append([x+1])
    for x in xrange(N):
    tree[x].append(findChildren(x+1))
    return tree

generateTree()

count = 0
for x in xrange(N):
    if len(tree[x][1]) % 2 == 1:
        count += 1
print count - 1