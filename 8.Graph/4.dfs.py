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

visited = [False] * n
ans=[]

def dfs(i,adjlist,visited):
    visited[i]=True
    ans.append(i)
    for x in adjlist[i]:
        if not visited[x]:
            dfs(x,adjlist,visited)


dfs(0,adjlist,visited)
print(ans)