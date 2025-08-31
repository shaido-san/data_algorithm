class EulerTour:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n)]
        self.timer = 0
        self.in_time = [0]*n
        self.out_time = [0]*n
        self.euler = []   # DFS順（in時だけ）

    def add_edge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)

    def dfs(self, v, p=-1):
        self.in_time[v] = self.timer
        self.euler.append(v)
        self.timer += 1
        for u in self.tree[v]:
            if u != p:
                self.dfs(u, v)
        self.out_time[v] = self.timer - 1  # 部分木の終端

    def build(self, root=0):
        self.dfs(root)

# ------------------------------
# デモ：部分木の和クエリ
# ------------------------------
if __name__ == "__main__":
    n = 5
    et = EulerTour(n)
    edges = [(0,1),(0,2),(2,3),(2,4)]
    for u,v in edges:
        et.add_edge(u,v)

    et.build(0)

    # ノードごとの値
    values = [5, 1, 4, 7, 3]

    # Euler Tour の配列に値を載せる
    base = [0]*n
    for v in range(n):
        base[et.in_time[v]] = values[v]

    # 部分木の和を区間 [in[v], out[v]] で取る
    def subtree_sum(v):
        l, r = et.in_time[v], et.out_time[v]
        return sum(base[l:r+1])

    print("in:", et.in_time)
    print("out:", et.out_time)
    print("euler:", et.euler)

    print("subtree sum of node 2 =", subtree_sum(2))  
    print("subtree sum of node 0 =", subtree_sum(0))  