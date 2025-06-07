class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text
        self._build_suffix_tree()

    def _insert_suffix(self, suffix, index):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
            node.indexes.append(index)

    def _build_suffix_tree(self):
        for i in range(len(self.text)):
            self._insert_suffix(self.text[i:], i)

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.indexes

# 使い方
text = "banana"
tree = SuffixTree(text)

print("ana found at:", tree.search("ana"))