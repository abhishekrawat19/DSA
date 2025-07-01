# BFS (BFS always implements through Queue)

# Custom Queue class
class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1  # Index to track the front element

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.queue.append(x)  # Add element to the end

    def pop(self):
        if len(self.queue) == 0:
            return -1  # Queue is empty
        x = self.queue[self.front]
        self.front += 1
        # Reset queue if all elements are popped
        if self.front == len(self.queue):
            self.queue = []
            self.front = -1
        return x

    def getfront(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1 or self.front >= len(self.queue)

# Edges of the graph
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]
n = 6  # number of nodes

# Adjacency list initialization
adjList = [] 
for i in range(n):
    adjList.append([])

# Filling the adjacency list
for edge in edges:
    x = edge[0]
    y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)  # because it's an undirected graph

# Display the adjacency list
for i in range(n):
    print(f"{i} ---> {adjList[i]}")

# Creating a queue object
q = Queue()

# BFS solution inside a class
class Solution:
    def __init__(self):
        self.ans = []

    def bfs(self, adjList, start_node):
        visited = [False] * len(adjList)  # Track visited nodes
        visited[start_node] = True
        self.ans.append(start_node)
        q.push(start_node)

        while q.is_empty() is False:
            x = q.pop()  # Current node
            for i in adjList[x]:  # Traverse neighbors
                if not visited[i]:
                    q.push(i)
                    self.ans.append(i)
                    visited[i] = True  # Mark as visited

        return self.ans

# Run BFS from node 0
sol = Solution()
result = sol.bfs(adjList, 0)
print("BFS Traversal:", result)
