my_list = [1, 3, 4, 6, 2]
target = my_list[4]

# 操作対象の要素より小さい値を持つ要素が見つかるまで一つ右側にずらす
j = 3 #要素の手前から処理を行う
while 0 <= j and target < my_list[j]:
    my_list[j + 1] = my_list[j]
    print(my_list)
    j -= 1

# ずらし終わったら開いたところに操作対象要素を設定
my_list[j + 1] = target
print(my_list)
