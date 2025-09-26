import bisect, hashlib

class ConsistentHash:
    def __init__(self, replicas=100):
        self.r=replicas; self.ring=[]; self.nodes={}
    def _h(self, s): return int(hashlib.md5(str(s).encode()).hexdigest(),16)
    def add(self, node):
        for i in range(self.r):
            h=self._h((node,i)); bisect.insort(self.ring,h); self.nodes[h]=node
    def remove(self, node):
        self.ring=[h for h in self.ring if self.nodes[h]!=node]; 
        self.nodes={h:n for h,n in self.nodes.items() if n!=node}
    def get(self, key):
        h=self._h(key); i=bisect.bisect(self.ring,h)%len(self.ring); return self.nodes[self.ring[i]]

ch=ConsistentHash()
for n in ["A","B","C"]: ch.add(n)
for k in ["user:1","user:2","user:9999"]: print(k,"->",ch.get(k))
ch.add("D"); print("after add D:", ch.get("user:9999"))