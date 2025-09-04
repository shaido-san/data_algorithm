class Node:
    def __init__(self, length, link):
        self.len = length
        self.link = link
        self.next = {}
        self.occ = 0
        self.pos = -1

class PalindromicTree:
    def __init__(self, s):
        self.s = s
        self.nodes = [Node(-1, 0), Node(0, 0)]
        self.suff = 1
        for i in range(len(s)):
            self.add(i)
        order = sorted(range(2, len(self.nodes)), key=lambda i: self.nodes[i].len, reverse=True)
        for v in order:
            self.nodes[self.nodes[v].link].occ += self.nodes[v].occ

    def get_link(self, v, i):
        while True:
            l = self.nodes[v].len
            if i - l - 1 >= 0 and self.s[i - l - 1] == self.s[i]:
                return v
            v = self.nodes[v].link

    def add(self, i):
        v = self.get_link(self.suff, i)
        c = self.s[i]
        if c in self.nodes[v].next:
            self.suff = self.nodes[v].next[c]
            self.nodes[self.suff].occ += 1
            return False
        cur = len(self.nodes)
        self.nodes.append(Node(self.nodes[v].len + 2, 0))
        self.nodes[cur].pos = i
        self.nodes[cur].occ = 1
        self.nodes[v].next[c] = cur
        if self.nodes[cur].len == 1:
            self.nodes[cur].link = 1
        else:
            u = self.nodes[v].link
            u = self.get_link(u, i)
            self.nodes[cur].link = self.nodes[u].next[c]
        self.suff = cur
        return True

    def distinct_count(self):
        return len(self.nodes) - 2

    def all_palindromes(self):
        res = []
        for i in range(2, len(self.nodes)):
            l = self.nodes[i].len
            p = self.nodes[i].pos
            res.append(self.s[p - l + 1:p + 1])
        return res

if __name__ == "__main__":
    s = "abacaba"
    t = PalindromicTree(s)
    print("distinct:", t.distinct_count())
    for i in range(2, len(t.nodes)):
        n = t.nodes[i]
        l = n.len
        p = n.pos
        sub = s[p - l + 1:p + 1]
        print(l, n.occ, sub)