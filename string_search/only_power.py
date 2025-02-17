def naive_search_text(text, pattern):

    # パターンとの照合回数を記録
    cnt = 0

    # パターン末尾のインデックス
    p_end_idx = len(pattern) - 1

    # テキスト側の照合開始位置を表すインデックス
    t_start_idx = 0
    while t_start_idx < len(text):
        
        # パターンとの照合回数をインクリメント
        cnt += 1

        # テキスト側の称号中の位置を表すインデックス
        t_idx = t_start_idx

        # パターン側の照合中の位置を表すインデックス
        p_idx = 0
        while t_idx < len(text) and text[t_idx] == pattern[p_idx]:
            if p_idx == p_end_idx:
                # パターン末尾まで一致していた場合、一致部分の先頭位置を返す
                print(cnt, "回パターンと照合しました")
                return t_start_idx
            
            # 照合位置を右側に一つずつ移動
            t_idx += 1
            p_idx += 1
        
        # テキスト側の照合開始位置を一つ移動
        t_start_idx += 1
    
    # 見つからない場合は-1を返す
    print(cnt, "回パターンと照合しました")
    return -1

def main():
    text = "Simple is better than complex."
    pattern="tha"
    idx = naive_search_text(text, pattern)
    print(idx)

main()


