def insertion_sort(my_list):
    for i in range(1, len(my_list)):

        # i番目の要素をソート対象として取り出す
        target = my_list[i]

        # 操作対象の要素より小さい値を持つ要素が見つかるまで一つ右側にずらす
        j = i - 1
        while 0 <= j and target < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        
        # ずらし終わったら開いたところに操作対象要素を設定
        my_list[j + 1] = target

        # 途中結果の確認のためダンプ
        print(my_list)

data = [6, 1, 4, 3, 2, 9, 8, 5, 10, 7]
print(data)
insertion_sort(data)
print(data)
        