from collections import deque

def topo_sort(graph):
    indegree = [0] * len(graph)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    q = deque([i for i in range(len(graph)) if indegree[i] == 0])
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return result

graph = {
    0: [1, 2],
    1: [2],
    2: []
}

print(topo_sort(graph))
              