def bellman_ford(edges, V, start):
    # ステップ1: 初期化
    dist = [float('inf')] * V
    dist[start] = 0

    # ステップ2: V-1回 緩和処理
    for i in range(V - 1):
        print(f"=== Step {i + 1} ===")
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                print(f"Updated: dist[{v}] = {dist[v]} (via {u} with cost {w})")
        print(f"Distances after step {i + 1}: {dist}\n")

    # ステップ3: 負の閉路チェック（あれば警告）
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative weight cycle detected!")
            return None

    return dist


# テスト用グラフ
edges = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]

V = 5  # 頂点数
start = 0

result = bellman_ford(edges, V, start)
print("== 最短距離 ==")
for i, d in enumerate(result):
    print(f"0 → {i}: {d if d != float('inf') else '∞'}")