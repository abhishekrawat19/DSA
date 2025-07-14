# Custom Stack class to simulate DFS manually
class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]

    def size(self):
        return len(self.st)

# Create a stack instance
stack = Stack()

# Number of nodes and edges
n = 6
e = 7

# Edge list
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

print(n, e, edges)

# ------------------------------
# Building adjacency list
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
# DFS traversal using Stack
class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, adjList, start_node):
        visited = [False] * len(adjList)
        visited[start_node] = True
        self.ans.append(start_node)
        stack.push(start_node)

        while stack.size() != 0:
            x = stack.pop()
            for i in adjList[x]:
                if not visited[i]:
                    stack.push(i)
                    self.ans.append(i)
                    visited[i] = True
        return self.ans

# Run DFS from node 0
sol = Solution()
result = sol.dfs(adjlist, 0)
print("DFS Traversal:", result)
