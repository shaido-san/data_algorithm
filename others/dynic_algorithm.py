from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t, level):
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] >= 0

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.graph[v])):
            it[v] = i
            to, cap, rev = self.graph[v][i]
            if cap > 0 and level[v] < level[to]:
                d = self.dfs(to, t, min(f, cap), level, it)
                if d > 0:
                    self.graph[v][i][1] -= d
                    self.graph[to][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        level = [-1]*self.n
        while self.bfs(s, t, level):
            it = [0]*self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0:
                    break
                flow += f
            level = [-1]*self.n
        return flow

if __name__ == "__main__":
    n = 4
    dinic = Dinic(n)
    dinic.add_edge(0, 1, 2)
    dinic.add_edge(0, 2, 1)
    dinic.add_edge(1, 2, 1)
    dinic.add_edge(1, 3, 1)
    dinic.add_edge(2, 3, 2)

    print("max flow =", dinic.max_flow(0, 3))