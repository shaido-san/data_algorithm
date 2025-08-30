from collections import defaultdict, deque

class PushRelabel:
    def __init__(self, n, s, t):
        self.n = n
        self.s = s
        self.t = t
        self.cap = defaultdict(int)      # cap[(u,v)] = capacity
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        # 有向辺 u->v （必要なら双方向に呼ぶ）
        if (u, v) not in self.cap and (v, u) not in self.cap:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.cap[(u, v)] += c

    def max_flow(self):
        n, s, t = self.n, self.s, self.t
        # 初期化
        height = [0]*n
        excess = [0]*n
        flow   = defaultdict(int)  # flow[(u,v)]

        def residual(u, v):
            # 残余容量
            return self.cap[(u, v)] - flow[(u, v)]

        def push(u, v):
            # u -> v に押し流す
            send = min(excess[u], residual(u, v))
            if send <= 0 or height[u] != height[v] + 1:
                return False
            flow[(u, v)] += send
            flow[(v, u)] -= send
            excess[u]    -= send
            excess[v]    += send
            return True

        def relabel(u):
            # u からどれも押せないなら高さを上げる
            min_h = float('inf')
            for v in self.adj[u]:
                if residual(u, v) > 0:
                    min_h = min(min_h, height[v])
            if min_h < float('inf'):
                height[u] = min_h + 1

        # 事前に全頂点ペア方向のcapキーを用意（逆辺0容量を明示）
        for u in range(n):
            for v in self.adj[u]:
                self.cap[(u, v)] = self.cap[(u, v)]  # ensure key
                self.cap[(v, u)] = self.cap[(v, u)]  # ensure reverse key

        # 初期前フロー：s の隣へ全押し
        height[s] = n
        for v in self.adj[s]:
            c = self.cap[(s, v)]
            if c > 0:
                flow[(s, v)] = c
                flow[(v, s)] = -c
                excess[v] += c
        excess[s] = -sum(self.cap[(s, v)] for v in self.adj[s])

        # アクティブ頂点（超過>0、s/t以外）を管理：Highest-Labelっぽく
        active_by_h = [deque() for _ in range(2*n)]
        max_h = 0
        for u in range(n):
            if u not in (s, t) and excess[u] > 0:
                active_by_h[height[u]].append(u)
                max_h = max(max_h, height[u])

        def activate(u):
            if u not in (s, t) and excess[u] > 0:
                active_by_h[height[u]].append(u)

        while max_h >= 0:
            if not active_by_h[max_h]:
                max_h -= 1
                continue
            u = active_by_h[max_h].pop()
            pushed = False
            for v in self.adj[u]:
                if excess[u] == 0:
                    break
                if push(u, v):
                    pushed = True
                    activate(v)
            if excess[u] > 0:  # まだ余ってる → relabel
                relabel(u)
                max_h = max(max_h, height[u])
                active_by_h[height[u]].append(u)

        # 最大フロー値は t の流入（= -flow[(t,*)]の総和）でも、sの流出総和でもOK
        maxflow = sum(flow[(u, t)] for u in range(n))
        return maxflow, flow

# -----------------------------
# デモ：グラフ作ってプリント
# -----------------------------
if __name__ == "__main__":
    # 例のネットワーク（CLRS系の定番に近い）
    # 頂点 0=s, 5=t
    n, s, t = 6, 0, 5
    pr = PushRelabel(n, s, t)
    edges = [
        (0,1,16), (0,2,13),
        (1,2,10), (1,3,12),
        (2,1,4),  (2,4,14),
        (3,2,9),  (3,5,20),
        (4,3,7),  (4,5,4),
    ]
    for u,v,c in edges:
        pr.add_edge(u, v, c)

    maxflow, flow = pr.max_flow()

    print("=== Push–Relabel 結果 ===")
    print("最大フロー:", maxflow)
    print("各辺のフロー（u->v: f / cap）")
    for u,v,c in edges:
        f = flow[(u,v)]
        print(f"{u}->{v}: {f} / {c}")