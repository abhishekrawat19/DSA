# Number of nodes and edges
n = 6
e = 7

# Undirected edge list
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

print(n, e, edges)

# ------------------------------
# Create adjacency list
adjlist = []
for i in range(n):
    adjlist.append([])

for edge in edges:
    x = edge[0]
    y = edge[1]
    adjlist[x].append(y)
    adjlist[y].append(x)

# Print adjacency list
for i in range(n):
    print(f"{i} --> {adjlist[i]}")

# ------------------------------
# DFS using recursion
visited = [False] * n
ans = []

def dfs(i, adjlist, visited):
    visited[i] = True
    ans.append(i)  # Add current node to answer

    for x in adjlist[i]:  # Visit all unvisited neighbors
        if not visited[x]:
            dfs(x, adjlist, visited)

# Call DFS from node 0
dfs(0, adjlist, visited)

# Print traversal order
print(ans)
