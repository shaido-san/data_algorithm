def bm_search_text(text, pattern):

    # パターンとの照合回数を記録
    cnt = 0

    # スキップテーブルの構築
    skip_table = build_skip_table(pattern)

    # パターンの長さ
    pattern_length = len(pattern)

    # パターン末尾のインデックス
    p_end_idx = len(pattern) - 1

    # テキスト側の照合位置のインデックス
    t_idx = len(pattern) - 1

    # 照合処理
    while t_idx < len(text):

        #照合パターンとの照合回数をインクリメント
        cnt += 1

        # パターン側の照合位置のインデックス（末尾からデクリメントする）
        p_idx = p_end_idx
        while text[t_idx] == pattern[p_idx]:

            if p_idx == 0:
                # パターンの末尾から1文字ずつ称号を行い、先頭まで同じ場合は一致したと判定
                print(cnt, "回パターンと照合しました")
                return t_idx
            
            # 照合する位置を左側に一つずつ移動
            t_idx -= 1
            p_idx -= 1
        
        # テキスト側の称号するインデックスをスキップテーブルの値に基づいて取得
        # ただし、スキップ後に位置が照合開始位置より左側になる場合は
        # pattern_length - p_idxをスキップ数とする
        skip_num = max(skip_table.get(text[t_idx], pattern_length), pattern_length - p_idx)

        # スキップ数分照合位置をスキップする
        t_idx += skip_num
    
    # 見つからない場合は-1を返す
    print(cnt, "回パターンと照合しました")
    return -1

def build_skip_table(pattern):
    skip_table = dict()
    pattern_length = len(pattern)
    for idx, char in enumerate(pattern[:-1]):
        skip_table[char] = pattern_length - idx -1
    
    return skip_table

# st1 = build_skip_table("abcd")
# print(st1)
# st2 = build_skip_table("abad")
# print(st2)

def main():
    text = "Simple is better than complex."
    pattern = "tha"
    idx = bm_search_text(text, pattern)
    print(idx)

main()

# st1 = build_skip_table("abcd")
# print(st1)
# st2 = build_skip_table("abad")
# print(st2)