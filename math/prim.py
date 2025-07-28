import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for cost, u, v in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))  # 無向グラフ

    visited = set()
    min_heap = [(0, 0)]  # (コスト, ノード)
    total_cost = 0
    mst_edges = []

    while len(visited) < n:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost

        for edge_cost, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_cost, v))
                mst_edges.append((u, v, edge_cost))

    return total_cost, mst_edges

n = 4  # ノードの数（0〜3）
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 2, 3),
    (5, 1, 3)
]

cost, mst = prim(n, edges)

print("最小コスト:", cost)
print("使われた道:", mst)