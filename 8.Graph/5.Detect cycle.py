# Detect cycle in an undirected graph (Unicycle Graph)

n = 6  # Number of nodes
e = 7  # Number of edges

# List of undirected edges (each pair represents a two-way connection)
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

# ------------------------------
# Step 1: Build the adjacency list
adjlist = []
for i in range(n):
    adjlist.append([])  # Create empty list for each node

# Fill the adjacency list with connections
for edge in edges:
    x, y = edge
    adjlist[x].append(y)  # Add y as a neighbor of x
    adjlist[y].append(x)  # Add x as a neighbor of y (since it's undirected)

# ------------------------------
# Step 2: DFS function to detect a cycle
visited = [False] * n  # Keeps track of visited nodes

def dfs(i, parent, adjlist, visited):
    visited[i] = True  # Mark current node as visited

    for x in adjlist[i]:  # Check all neighbors of node i
        if x == parent:
            continue  # Skip the node we just came from

        if visited[x]:
            return True  # If neighbor already visited and not parent → cycle detected

        if dfs(x, i, adjlist, visited):  # Recur on unvisited neighbor
            return True  # If any recursive call detects a cycle, return True
    
    return False  # No cycle found along this path

# ------------------------------
# Step 3: Start DFS from node 0
# Initial parent is -1 (no parent, since 0 is the starting node)
cx = dfs(0, -1, adjlist, visited)

# Output the result
print(cx)  # True if a cycle exists, False otherwise
