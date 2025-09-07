import heapq

def bellman_ford(n, edges, src):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(n-1):
        update = False
        for u,v,w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                update = True
        if not update:
            break
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist

def dijkstra(n, adj, src):
    dist = [float("inf")] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d,u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v,w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def johnson(n, edges):
    q = n
    new_edges = edges + [(q, v, 0) for v in range(n)]
    h = bellman_ford(n+1, new_edges, q)
    if h is None:
        raise ValueError("Negative cycle detected")
    adj = [[] for _ in range(n)]
    for u,v,w in edges:
        adj[u].append((v, w + h[u] - h[v]))
    all_pairs = []
    for u in range(n):
        dist_prime = dijkstra(n, adj, u)
        dist = [d + h[v] - h[u] if d < float("inf") else float("inf") for v,d in enumerate(dist_prime)]
        all_pairs.append(dist)
    return all_pairs

if __name__ == "__main__":
    n = 5
    edges = [
        (0,1,-1),
        (0,2,4),
        (1,2,3),
        (1,3,2),
        (1,4,2),
        (3,2,5),
        (3,1,1),
        (4,3,-3),
    ]
    dist = johnson(n, edges)
    for u in range(n):
        print(f"from {u}:", dist[u])