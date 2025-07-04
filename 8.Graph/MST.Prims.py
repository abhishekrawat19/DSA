# Prims Algorithm using iterative approach


adjmatrix=[[0,9,75,0,0],[9,0,95,19,42],
           [75,95,0,51,66],[0,19,51,0,31],
           [0,42,66,31,0]
           ]


n=5
visited=[False]*n
visited[0]=True
ans=0
for _ in range(n-1): # n-1
    x=-1
    y=-1
    min=float("inf")
    for i in range(n): # i visited 
        for j in range(n): # j not visited
            if adjmatrix[i][j]!=0 and visited[i] and not visited[j]:
                if adjmatrix[i][j]<min:
                    min=adjmatrix[i][j]
                    x=i
                    y=j
    ans+=min
    visited[y]=True



print(ans)