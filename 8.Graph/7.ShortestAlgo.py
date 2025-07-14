import heapq

def shortestPath(n, edges, s):
    # Step 1: Create adjacency list
    adjlist = [[] for _ in range(n)]
    for edge in edges:
        x, y, w = edge
        adjlist[x].append([y, w])
        adjlist[y].append([x, w])  # Undirected graph

    # Step 2: Initialize min-heap and distance array
    heap = []
    dist = [float("inf")] * n
    dist[s] = 0

    # Push the source node into the heap
    heapq.heappush(heap, (dist[s], s))  # (distance, node)

    # Step 3: Dijkstra's loop
    while len(heap) > 0:
        d, u = heapq.heappop(heap)  # Pop the node with the smallest distance

        for v, w in adjlist[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w  # ← Corrected line!
                heapq.heappush(heap, (dist[v], v))

    # Step 4: Return final distances
    return dist
