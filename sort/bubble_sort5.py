def bubble_sort(arr):
    """
    バブルソート（Bubble Sort）
    - 隣り合う要素を比較し、大小を入れ替えながらリストを並べ替える。
    - 大きい値がどんどん右に移動し、最後に確定する（泡が上に上がるイメージ）。
    - 計算量は O(N²) なので、大きなデータには向かない。
    """

    n = len(arr)  # リストの長さ

    for i in range(n):  # 外側のループ（n回実行）
        swapped = False  # 交換が発生したかを記録

        for j in range(n - 1 - i):  # 内側のループ（隣同士を比較）
            print(f"比較: {arr[j]} と {arr[j+1]}", end="  ")

            if arr[j] > arr[j + 1]:  # 大きい方が前なら交換
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # 交換が発生
                print(f"→ 交換: {arr}")
            else:
                print("→ 交換なし")

        if not swapped:  # 交換が1度も発生しなければ終了（既にソート済み）
            break

    return arr  # ソート後のリストを返す


# 【テスト】
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("🔍 ソート前:", unsorted_list)
sorted_list = bubble_sort(unsorted_list)
print("\n✅ ソート後:", sorted_list)