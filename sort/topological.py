from collections import defaultdict, deque

class TopologicalSorter:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1
        if u not in self.in_degree:
            self.in_degree[u] = 0  # 初期化

    def sort(self):
        queue = deque([node for node in self.in_degree if self.in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(self.in_degree):
            raise ValueError("グラフにサイクルがあります！トポロジカルソートできません。")
        return result


# 使い方
sorter = TopologicalSorter()
sorter.add_edge('A', 'B')
sorter.add_edge('B', 'C')
sorter.add_edge('A', 'C')
sorter.add_edge('C', 'D')

try:
    order = sorter.sort()
    print("トポロジカルソート結果:", order)
except ValueError as e:
    print(e)