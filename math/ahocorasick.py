from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

class AhoCorasick:
    def __init__(self, keywords):
        self.root = TrieNode()
        for keyword in keywords:
            self._insert(keyword)
        self._build_fail_links()

    def _insert(self, keyword):
        node = self.root
        for char in keyword:
            node = node.children.setdefault(char, TrieNode())
        node.output.append(keyword)

    def _build_fail_links(self):
        queue = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                fail_node = current.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children[char] if fail_node else self.root
                child.output += child.fail.output if child.fail else []
                queue.append(child)

    def search(self, text):
        node = self.root
        results = []
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[char]
            for match in node.output:
                results.append((i - len(match) + 1, match))
        return results

# 実行例
ac = AhoCorasick(['he', 'she', 'his', 'hers'])
text = 'ushers'
print(ac.search(text))  # => [(1, 'she'), (2, 'he'), (2, 'hers')]