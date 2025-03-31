class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        # シンボル
        self.symbol = symbol

        # 頻度
        self.freq = freq

        # 左子
        self.left = left

        # 右子
        self.right = right

        # 符号
        self.code = ''
    
    def __lt__(self, other):
        # 比較演算の定義
        return self.freq < other.freq
    
    def __str__(self):
        return self.symbol

def build_code_dict(node, parent_code, result_dict):
    
    # 頂点ノードから再帰敵にハフマン符号化の符号辞書を構築する
    current_code = parent_code + node.code

    # 左右いずれかに子がある場合、再帰的に処理を行う
    if node.left:
        build_code_dict(node.left, current_code, result_dict)
    if node.right:
        build_code_dict(node.right, current_code, result_dict)
    
    # 子がない場合はリーフノードなので結果をresult_dictに格納する
    if not (node.left or node.right):
        result_dict[node.symbol] = current_code

def compress(text, codes):
    compressed = ""
    for c in text:
        code = codes.get(c)
        compressed += code
    return compressed

def decompress(compressed, codes):
    swapped_codes = {v: k for k, v in codes.items()}
    decompressed = ""
    code = ""
    for c in compressed:
        code += c
        value = swapped_codes.get(code)
        if value:
            decompressed += value
            code = ""
    
    print(decompressed)

def aggregate_frequency(text):
    freq: dict = dict()
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)

freq_list = aggregate_frequency("BDDAAAABACEBBBAA")

def build_huffman_tree(text):

    # 頻度のリスト
    freq_list = aggregate_frequency(text)

    # ノード格納ようのリスト
    nodes = []

    # ノードリストを構築
    for symbol, freq in freq_list:
        node = Node(symbol, freq)
        nodes.append(node)
    
    # ループ処理では不満ツリーを構築（要素数が２以上の間ループを継続する）
    while 2 <= len(nodes):

        # 降順にソート
        nodes = sorted(nodes, reverse=True)

        # 要素を末端からふたつ取り出す
        right = nodes.pop(-1)
        left = nodes.pop(-1)

        # それぞれのノードに符号を割り当て（左＝０、右＝１）
        left.code = "0"
        right.code = "1"

        # 親ノードparentを生成
        # このシンボルを結合したものを親のシンボルとする
        parent_symbol = left.symbol + right.symbol

        # この頻度を合算したものを親の頻度とする
        parent_freq = left.freq + right.freq
        parent = Node(parent_symbol, parent_freq, left, right)

        # ノードリストの末尾にparentを追加する
        nodes.append(parent)
    
    # ここで符号化が完了
    root = nodes[0]

    # 以下、符号化結果を表示
    result_dict = dict()
    build_code_dict(root, "", result_dict)
    print(result_dict)

build_huffman_tree("BDDAAAABACEBBBAA")
