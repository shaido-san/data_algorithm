from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = [{}]         
        self.fail = [0]          
        self.output = [set()]    

    def add_word(self, word):
        node = 0
        for ch in word:
            if ch not in self.trie[node]:
                self.trie[node][ch] = len(self.trie)
                self.trie.append({})
                self.fail.append(0)
                self.output.append(set())
            node = self.trie[node][ch]
        self.output[node].add(word)

    def build(self):
        q = deque()
        for ch, nxt in self.trie[0].items():
            q.append(nxt)
            self.fail[nxt] = 0

        while q:
            r = q.popleft()
            for ch, u in self.trie[r].items():
                q.append(u)
                v = self.fail[r]
                while v and ch not in self.trie[v]:
                    v = self.fail[v]
                self.fail[u] = self.trie[v].get(ch, 0)
                self.output[u] |= self.output[self.fail[u]]

    def search(self, text):
        node = 0
        results = []
        for i, ch in enumerate(text):
            while node and ch not in self.trie[node]:
                node = self.fail[node]
            node = self.trie[node].get(ch, 0)
            for word in self.output[node]:
                results.append((i - len(word) + 1, word))
        return results


ac = AhoCorasick()
for w in ["quick", "brown", "lazy"]:
    ac.add_word(w)
ac.build()

text = "the quick brown fox jumps over the lazy dog"
print(ac.search(text))