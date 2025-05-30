class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return False
        return node.is_end

trie = Trie()
words = ["cat", "cap", "can", "bat"]
for word in words:
    trie.insert(word)

tests = ["cat", "cap", "bat", "cat"]
for word in tests:
    print(f"{word}:", "見つかった" if trie.search(word) else "ないです")