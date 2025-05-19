def tarjans_scc(graph):
    n = len(graph)
    index = 0
    indices = [-1] * n
    lowlink = [0] * n
    stack = []
    on_stack = [False] * n
    result = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)

    return result

graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: []
}
print(tarjans_scc(graph))
