# Detected cycle in Unicycle Graph
n=6
e=7

edges= [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] # edges

# adjacent list 
adjlist=[]
for i in range(n):
    adjlist.append([])

for edge in edges:
    x=edge[0]
    y=edge[1]

    adjlist[x].append(y)
    adjlist[y].append(x)


visited=[False]*n

def dfs(i,parent,adjlist,visited):
    visited[i]=True

    for x in adjlist[i]:
        if x==parent:
            continue
        if visited[x]:
            return True
        if dfs(x,i,adjlist,visited):
            return True
        
    return False


cx=dfs(0,-1,adjlist,visited)
print(cx)