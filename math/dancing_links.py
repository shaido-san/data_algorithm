class Node:
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None

class Column(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.size = 0

def link_nodes(matrix, column_names):
    header = Column("header")
    columns = []
    last = header
    for name in column_names:
        col = Column(name)
        columns.append(col)
        col.left = last
        col.right = header
        last.right = col
        header.left = col
        last = col

    for row in matrix:
        prev = None
        for j, cell in enumerate(row):
            if cell:
                node = Node()
                node.column = columns[j]
                # 縦リンク
                node.up = columns[j].up
                node.down = columns[j]
                columns[j].up.down = node
                columns[j].up = node
                columns[j].size += 1
                # 横リンク
                if prev:
                    node.left = prev
                    node.right = prev.right
                    prev.right.left = node
                    prev.right = node
                else:
                    prev = node
                    node.left = node
                    node.right = node
    return header

def cover(col):
    col.right.left = col.left
    col.left.right = col.right
    i = col.down
    while i != col:
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down
            j.column.size -= 1
            j = j.right
        i = i.down

def uncover(col):
    i = col.up
    while i != col:
        j = i.left
        while j != i:
            j.column.size += 1
            j.down.up = j
            j.up.down = j
            j = j.left
        i = i.up
    col.right.left = col
    col.left.right = col

def search(header, solution):
    if header.right == header:
        print("解:", [n.column.name for n in solution])
        return True
    col = min((c for c in iter_cols(header)), key=lambda c: c.size)
    cover(col)
    r = col.down
    while r != col:
        solution.append(r)
        j = r.right
        while j != r:
            cover(j.column)
            j = j.right
        if search(header, solution):
            return True
        solution.pop()
        j = r.left
        while j != r:
            uncover(j.column)
            j = j.left
        r = r.down
    uncover(col)
    return False

def iter_cols(header):
    c = header.right
    while c != header:
        yield c
        c = c.right

matrix = [
    [1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0],
    [0,0,0,1,1,0,1],
    [0,0,1,0,1,1,0],
    [0,1,1,0,0,1,1],
    [0,1,0,0,0,0,1],
]
header = link_nodes(matrix, ["C1","C2","C3","C4","C5","C6","C7"])
search(header, [])