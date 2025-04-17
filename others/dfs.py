class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        self.edges.setdefault(u, []).append(v)
        self.edges.setdefault(v, []).append(u)  # 無向グラフとして

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(f"訪問: {start}")
        for neighbor in self.edges.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# 呼び出し
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("DFS開始")
g.dfs(1)