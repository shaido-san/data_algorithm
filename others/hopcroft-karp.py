from collections import deque

class HopcroftKarp:
    def __init__(self, n_left, n_right):
        self.nL = n_left
        self.nR = n_right
        self.adj = [[] for _ in range(n_left)]
        self.dist = [0]*(n_left+1)
        self.matchL = [-1]*n_left
        self.matchR = [-1]*n_right

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self):
        q = deque()
        for u in range(self.nL):
            if self.matchL[u] == -1:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = -1
        found = False
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if self.matchR[v] != -1 and self.dist[self.matchR[v]] == -1:
                    self.dist[self.matchR[v]] = self.dist[u] + 1
                    q.append(self.matchR[v])
                if self.matchR[v] == -1:
                    found = True
        return found

    def dfs(self, u):
        for v in self.adj[u]:
            if self.matchR[v] == -1 or (self.dist[self.matchR[v]] == self.dist[u]+1 and self.dfs(self.matchR[v])):
                self.matchL[u] = v
                self.matchR[v] = u
                return True
        self.dist[u] = -1
        return False

    def max_matching(self):
        match = 0
        while self.bfs():
            for u in range(self.nL):
                if self.matchL[u] == -1 and self.dfs(u):
                    match += 1
        return match

if __name__ == "__main__":
    nL, nR = 4, 4
    hk = HopcroftKarp(nL, nR)
    edges = [(0,0),(0,1),(1,1),(2,2),(3,2),(3,3)]
    for u,v in edges:
        hk.add_edge(u,v)

    print("max matching =", hk.max_matching())
    print("matchL:", hk.matchL)
    print("matchR:", hk.matchR)