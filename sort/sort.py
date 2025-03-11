def selection_sort(arr):
    """
    選択ソート（Selection Sort）
    - 最小値を探して、左端と交換することで並び替えを行う。
    - 計算量は O(N²)。シンプルだが、効率は良くない。
    """

    n = len(arr)  # 配列の長さを取得

    # 配列の左端から順番に処理していく
    for i in range(n):
        # 1. 最小値のインデックスを現在位置（i）で初期化
        min_index = i

        # 2. iの次から最後まで走査して、最小値を探す
        for j in range(i + 1, n):
            print(f"比較: {arr[min_index]} と {arr[j]}")
            if arr[j] < arr[min_index]:
                min_index = j  # より小さい値が見つかったら更新

        # 3. 最小値が現在のiと異なれば交換
        if min_index != i:
            print(f"交換: {arr[i]} と {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"ステップ {i + 1} 回目: {arr}")

    return arr  # ソート済み配列を返す


# 【テストデータ】
unsorted_list = [64, 25, 12, 22, 11]
print("🔍 ソート前:", unsorted_list)

sorted_list = selection_sort(unsorted_list)

print("\n✅ ソート後:", sorted_list)