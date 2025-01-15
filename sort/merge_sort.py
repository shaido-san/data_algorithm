# リストの個数と、リストの内容を入力するとマージソートされる。

import sys

INF = 1000000001
count = 0

def merge(a, left, mid, right):
    global count
    nl = mid - left
    nr = right - mid

    # 左右の部分配列を作成
    l = a[left:mid] + [INF]
    r = a[mid:right] + [INF]

    l_index = 0
    r_index = 0

    # マージ処理
    for i in range(left, right):
        if l[l_index] < r[r_index]:
            a[i] = l[l_index]
            l_index += 1
        else:
            a[i] = r[r_index]
            r_index += 1
            count += 1 # 右から取り出す場合の比較関数をカウント

def merge_sort(a, left, right):
    if left >= right - 1:
        return
    
    mid = (left + right) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)
    merge(a, left, mid, right)

def main():
    global count

    # 入力を受け取る
    n = int(input())
    a = list(map(int, input().split()))

    # マージソートを実行
    merge_sort(a, 0, n)

    # ソート結果を出力
    print(" ".join(map(str, a)))

    # 比較回数を出力
    print(count)

if __name__ == "__main__":
    main()
