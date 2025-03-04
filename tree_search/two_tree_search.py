class Node:
    def __init__(self, key, value, is_left=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.is_left = is_left
    
    def __str__(self):
        return str(self.key) + ":" + str(self.value)
    

class BsTree:
    def __init__(self):
        self.root = None
    
    def add(self, key, value):
        # rootがない場合はrootに設定
        if self.root is None:
            self.root = Node(key, value)
            return
    
        self._add_node(self.root, key, value)
    
    def _add_node(self, node, key ,value):
        if key == node.key:
            print("指定したキーはすでに存在するため追加できませんでした", key)
            return
        
        if key < node.key:
            # 指定したキーが現在のノードのキーより小さい場合
            if not node.left:
                # 左に空きがあればそこに設定
                node.left = Node(key, value, is_left=True)
                return
            else:
                # 左に空きがなければ左側を再起的にたどる
                self._add_node(node.left, key, value)
        
        else:
            # 指定したキーが現在のノードのキーより大きい場合
            if not node.right:
                # 右側に空きがあればそこに設定
                node.right = Node(key, value, is_left=False)
                return
            else:
                # 右側に空きがなければ右側を再起的にたどる
                self._add_node(node.right, key, value)
    
    def get(self, key):
        return self._get_node(self.root, key)
    
    def _get_node(self, node, key):
        if node is None:
            print("指定したキーのノードは見つかりませんでした")
            return node
        
        if key == node.key:
            # 引数で指定したキーとノードのキーが一致
            return node
        
        # ルートから指定したキーのノードまで再起的にたどる
        if key < node.key:
            # 指定したキーが現在のノードのキーより小さい場合、左側を再起的にたどる
            return self._get_node(node.left, key)
        else:
            # 指定したキーが現在のノードのキーより大きい場合、右側を再起的にたどる
            return self._get_node(node.right, key)

def main():
    bst = BsTree()
    bst.add(5, "Yamada")
    bst.add(3, "Tanaka")
    bst.add(8, "Suzuki")
    bst.add(7, "Sato")
    bst.add(9, "Takahashi")
    bst.add(1, "Watanabe")

    node = bst.get(7)
    print(node)

main()
