class CentroidDecomposition:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n)]
        self.subtree_size = [0]*n
        self.centroid_parent = [-1]*n
        self.used = [False]*n

    def add_edge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)

    def dfs_size(self, v, p=-1):
        self.subtree_size[v] = 1
        for u in self.tree[v]:
            if u != p and not self.used[u]:
                self.dfs_size(u, v)
                self.subtree_size[v] += self.subtree_size[u]

    def find_centroid(self, v, p, total_size):
        for u in self.tree[v]:
            if u != p and not self.used[u]:
                if self.subtree_size[u] > total_size // 2:
                    return self.find_centroid(u, v, total_size)
        return v

    def build(self, v=0, p=-1):
        self.dfs_size(v)
        c = self.find_centroid(v, -1, self.subtree_size[v])
        self.centroid_parent[c] = p
        self.used[c] = True
        for u in self.tree[c]:
            if not self.used[u]:
                self.build(u, c)
        return c

if __name__ == "__main__":
    n = 7
    cd = CentroidDecomposition(n)
    edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
    for u,v in edges:
        cd.add_edge(u,v)

    root = cd.build(0)

    print("Centroid Decomposition Tree (親配列):", cd.centroid_parent)
    print("Root centroid:", root)