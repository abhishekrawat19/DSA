class Stack:
    def __init__(self):
        self.st=[]

    
    def push(self,x):
        self.st.append(x)

    def pop(self):
        if len(self.st)==0:
            return -1
        
        x=self.st[-1]
        self.st.pop()
        return x
    
    def top(self):
        if len(self.st)==0:
            return -1
        return self.st[-1]
    
    def size(self):
        return len(self.st)
    

stack =Stack()
n=6
e=7

edges= [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] # edges

print(n,e,edges)

# adjacent list 
adjlist=[]
for i in range(n):
    adjlist.append([])

for edge in edges:
    x=edge[0]
    y=edge[1]

    adjlist[x].append(y)
    adjlist[y].append(x)

for i in range(n):
    print(f"{i} --> {adjlist[i]}")


# BFS solution inside a class
class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, adjList, start_node):
        visited = [False] * len(adjList)  # Track visited nodes
        visited[start_node] = True
        self.ans.append(start_node)
        stack.push(start_node)

        while stack.size() != 0:
            x = stack.pop()  # Current node
            for i in adjList[x]:  # Traverse neighbors
                if not visited[i]:
                    stack.push(i)
                    self.ans.append(i)
                    visited[i] = True  # Mark as visited

        return self.ans

# Run BFS from node 0
sol = Solution()
result = sol.dfs(adjlist, 0)
print("DFS Traversal:", result)
