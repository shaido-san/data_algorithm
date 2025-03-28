def my_rle(my_string):
    # 指定した文字列をランレングスで圧縮する

    # 圧縮結果を格納するリスト
    result_list = []

    # 各データの個数を格納するカウンタ
    counter = 1

    # 0番目の文字列をあらかじめ格納
    pre_char = my_string[0]

    # 1番目の文字列からループ処理を行う
    for char in my_string[1:]:

        # 一つ手前の文字列と等しい場合、カウンタをインクリメントする
        if char == pre_char:
            counter += 1
        
        else:
            result_list.append((pre_char, counter))
            counter = 1
        pre_char = char
    
    # 最後の文字列とそのカウンタの値を格納する
    result_list.append((pre_char, counter))
    print(result_list)

my_rle("AAAAAAAAAABBBBBCCCCCCCC")

