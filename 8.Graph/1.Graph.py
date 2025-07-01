# Graph 

n=6
e=7

edges= [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] # edges

print(n,e,edges)

# adjacent list 
adjList=[]
for i in range(n):
    adjList.append([])

for edge in edges:
    x=edge[0]
    y=edge[1]

    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(f"{i} --> {adjList[i]}")


# adjacenMatrix
adjmatrix=[]
for i in range(n):
    adjmatrix.append([-1]*n)


for edge in edges:
    x=edge[0]
    y=edge[1]

    adjmatrix[x][y]=1
    adjmatrix[y][x]=1


for i in adjmatrix:
    print(i)
