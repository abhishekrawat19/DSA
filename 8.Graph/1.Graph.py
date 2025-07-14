# Graph Representation in Python

# Number of nodes and edges
n = 6  # nodes from 0 to 5
e = 7  # total number of edges

# List of edges (undirected)
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

print(n, e, edges)

# ------------------------------
# 1. Adjacency List Representation
# ------------------------------

# Initialize an empty adjacency list
adjList = []
for i in range(n):
    adjList.append([])  # Create an empty list for each node

# Populate the adjacency list
for edge in edges:
    x = edge[0]
    y = edge[1]
    
    adjList[x].append(y)  # Add y to the list of x
    adjList[y].append(x)  # Add x to the list of y (because the graph is undirected)

# Display the adjacency list
print("\nAdjacency List:")
for i in range(n):
    print(f"{i} --> {adjList[i]}")

# ------------------------------
# 2. Adjacency Matrix Representation
# ------------------------------

# Initialize an adjacency matrix filled with -1
adjMatrix = []
for i in range(n):
    adjMatrix.append([-1] * n)

# Populate the adjacency matrix
for edge in edges:
    x = edge[0]
    y = edge[1]
    
    adjMatrix[x][y] = 1  # There is an edge from x to y
    adjMatrix[y][x] = 1  # There is an edge from y to x (undirected)

# Display the adjacency matrix
print("\nAdjacency Matrix:")
for row in adjMatrix:
    print(row)
