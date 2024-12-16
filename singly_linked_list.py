class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class SinglyLinkedList:
    def __init__(self, head_value):
        self.head = Node(head_value)
    
    def append(self, value):
        
        #新たにノードを生成
        new_node = Node(value)

        #先頭から順にリンクが設定されていないノード（＝終端ノード）までたどる
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        #終端ノードのnextに生成したnodeを設定する
        current_node.next = new_node

    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node))
            current_node = current_node.next
            
        return "-".join(nodes)
    
    #current_nodeはリンクリスト内で現在操作中のノードを指す変数。
    #current_idxはリンクリスト内で現在のノードが何番目かを追跡するための変数
    def get(self, idx):
        #先頭からidx番目までノードをたどる
        current_node = self.head
        current_idx = 0
        while current_node and current_idx < idx:
            current_node = current_node.next
            current_idx += 1
        
        return current_node
    
    def insert(self, idx, value):
        #新たにノード生成
        new_node = Node(value)

        #先頭への挿入の場合、headを付け替え
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        #先頭以外の場合はidxの一つ前の要素を取得
        pre_node = self.get(idx - 1)

        #指定した要素が見つからない場合は終了

        if not pre_node:
            print("Can't insert")
            return
        
        #参照先を付け替え挿入
        new_node.next = pre_node.next
        pre_node.next = new_node
    
    def delete(self, idx):
        if idx == 0:
            if not self.head:
                print("Can't (delette)")
            else:
                self.head = self.head.next
            
            return
        
        #先頭以外の場合、idxの一つ前の要素と当該要素を取得
        pre_node = self.get(idx - 1)
        if not pre_node:
            print("Can't delete")
            return
        
        target_node = pre_node.next
        if not target_node:
            print("Can't delete")
            return
        
        #参照先を付け替え削除
        pre_node.next = target_node.next

my_list = SinglyLinkedList(35)
my_list.append(22)
my_list.append(8)
print(my_list)
my_list.delete(1)
print(my_list)
#deleteメソッド追加のため確認コマンドを変更する
# my_list.insert(2, 72)
#insertメソッド追加のため、確認コマンドを変更する
# x = my_list.get(0)
# y = my_list.get(1)
# z = my_list.get(2)
# print(x, y, z)
#getメソッドを追加したため、確認コマンドを変更する
# my_list.append(8)
# print(my_list)
# my_list.append(15)
# print(my_list)