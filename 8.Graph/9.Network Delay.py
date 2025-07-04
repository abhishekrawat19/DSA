import heapq

def shortestPath(n,edges,s):
    adjlist=[]
    for i in range(n):
        adjlist.append([])


    for edge in edges:
        x=edge[0]
        y=edge[1]
        w=edge[2]

        adjlist[x].append([y,w])
    heap=[]
    dist=[float("inf")]*n

    dist[s]=0
    heapq.heappush(heap,(dist[s],s))

    while len(heap)>0:
        d,u=heapq.heappop(heap)

        for v,w in adjlist[u]:
            if dist[u] + w < dist[v]:
                dist[v]=dist[v]+w
                heapq.heappush(heap,(dist[v],v))