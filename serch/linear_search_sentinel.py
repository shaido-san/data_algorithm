def liner_search_sentinel(my_list, val):
    idx = 0
    N = len(my_list)
    # 番兵を末尾に追加
    my_list.append(val)

    while True:
        if my_list[idx] == val:
            break
        idx += 1
    
    if idx == N:
        print("見つかりませんでした")
    
    else:
        print(str(idx) + "番目に見つかりました")

l = [1, 5, 9, 6, 2, 8, 4, 0]
liner_search_sentinel(l, 8)
liner_search_sentinel(l, 4)