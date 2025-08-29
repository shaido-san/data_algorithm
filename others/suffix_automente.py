class State:
    def __init__(self):
        self.next = {}   
        self.link = -1   
        self.len = 0     

class SuffixAutomaton:
    def __init__(self):
        self.states = [State()]
        self.last = 0  # 直前の状態

    def extend(self, c):
        p = self.last
        cur = len(self.states)
        self.states.append(State())
        self.states[cur].len = self.states[p].len + 1

        while p >= 0 and c not in self.states[p].next:
            self.states[p].next[c] = cur
            p = self.states[p].link

        if p == -1:
            self.states[cur].link = 0
        else:
            q = self.states[p].next[c]
            if self.states[p].len + 1 == self.states[q].len:
                self.states[cur].link = q
            else:
                clone = len(self.states)
                self.states.append(State())
                self.states[clone].len = self.states[p].len + 1
                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].link = self.states[q].link
                while p >= 0 and self.states[p].next.get(c) == q:
                    self.states[p].next[c] = clone
                    p = self.states[p].link
                self.states[q].link = self.states[cur].link = clone
        self.last = cur

def count_substrings(s):
    sam = SuffixAutomaton()
    for ch in s:
        sam.extend(ch)
    res = 0
    for i, st in enumerate(sam.states):
        if st.link != -1:
            res += st.len - sam.states[st.link].len
    return res

print(count_substrings("aba")) 