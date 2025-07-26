class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  
        self.parent[root_y] = root_x
        return True

def kruskal(n, edges):
    """
    n: 頂点の数（0〜n-1）
    edges: (コスト, 頂点A, 頂点B) のリスト
    """
    uf = UnionFind(n)
    edges.sort()  
    mst_cost = 0
    mst_edges = []

    for cost, u, v in edges:
        if uf.union(u, v):  
            mst_cost += cost
            mst_edges.append((u, v, cost))
    
    return mst_cost, mst_edges

n = 4  

edges = [
    (1, 0, 1),  
    (3, 0, 2),
    (2, 1, 2),
    (4, 2, 3),
    (5, 1, 3)
]

cost, result = kruskal(n, edges)

print("最小コスト:", cost)
print("選ばれた道:", result)