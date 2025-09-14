class GabowSCC:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.S = []
        self.P = []
        self.index = [None]*n
        self.comp_id = [-1]*n
        self.time = 0
        self.sccs = []

    def add_edge(self,u,v):
        self.g[u].append(v)

    def dfs(self,v):
        self.index[v] = self.time
        self.time += 1
        self.S.append(v)
        self.P.append(v)
        for u in self.g[v]:
            if self.index[u] is None:
                self.dfs(u)
            elif self.comp_id[u] == -1:
                while self.index[self.P[-1]] > self.index[u]:
                    self.P.pop()
        if self.P and self.P[-1] == v:
            comp = []
            while True:
                x = self.S.pop()
                self.comp_id[x] = len(self.sccs)
                comp.append(x)
                if x == v:
                    break
            self.P.pop()
            self.sccs.append(comp)

    def scc(self):
        for v in range(self.n):
            if self.index[v] is None:
                self.dfs(v)
        return self.sccs

if __name__ == "__main__":
    g = GabowSCC(8)
    edges = [
        (0,1),(1,2),(2,0),
        (3,1),(3,2),(3,4),
        (4,5),(5,6),(6,4),
        (6,7)
    ]
    for u,v in edges:
        g.add_edge(u,v)
    sccs = g.scc()
    print("SCCs:", sccs)