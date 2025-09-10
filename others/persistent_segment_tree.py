class Node:
    __slots__ = ("left","right","val")
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

def build(l, r):
    if l == r:
        return Node(val=0)
    m = (l+r)//2
    return Node(build(l,m), build(m+1,r), 0)

def update(prev, l, r, idx, delta):
    if l == r:
        return Node(val=prev.val+delta)
    m = (l+r)//2
    if idx <= m:
        return Node(update(prev.left, l, m, idx, delta), prev.right, prev.val+delta)
    else:
        return Node(prev.left, update(prev.right, m+1, r, idx, delta), prev.val+delta)

def query(node, l, r, ql, qr):
    if qr < l or r < ql: return 0
    if ql <= l and r <= qr: return node.val
    m = (l+r)//2
    return query(node.left,l,m,ql,qr)+query(node.right,m+1,r,ql,qr)

if __name__ == "__main__":
    n = 5
    root0 = build(0,n-1)

    root1 = update(root0,0,n-1,2,5)  # arr[2]+=5
    root2 = update(root1,0,n-1,4,3)  # arr[4]+=3
    root3 = update(root2,0,n-1,2,2)  # arr[2]+=2

    print("v0 sum[0..4] =", query(root0,0,n-1,0,4))
    print("v1 sum[0..4] =", query(root1,0,n-1,0,4))
    print("v2 sum[0..4] =", query(root2,0,n-1,0,4))
    print("v3 sum[0..4] =", query(root3,0,n-1,0,4))
    print("v2 sum[2..4] =", query(root2,0,n-1,2,4))