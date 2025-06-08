class Node:
    def __init__(self, name=None):
        self.children = {}
        self.suffix_link = None
        self.start = -1
        self.end = -1
        self.name = name

    def __repr__(self):
        return f"Node({self.name})"

root = Node()
node_abc = Node(name="abc")
node_bc = Node(name="bc")

root.children['a'] = node_abc
node_abc.children['b'] = node_bc

node_abc.suffix_link = node_bc

print("abcノードのsuffix link先は：", node_abc.suffix_link)