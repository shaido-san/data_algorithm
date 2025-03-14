def insertion_sort(arr):
    """
    挿入ソート（Insertion Sort）
    - 整列済み部分列に対して、新しい要素を正しい位置に挿入する。
    - 「トランプの手札を並べる」イメージ。
    """

    n = len(arr)  # 配列の長さ

    # 1つ目の要素はすでに整列済みとみなす（i=1から開始）
    for i in range(1, n):
        current_value = arr[i]  # 今回挿入する値
        position = i - 1        # 整列済み部分の最後のインデックス

        print(f"\n🔎 挿入する値: {current_value}")

        # 整列済み部分を右にずらしながら、挿入位置を探す
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]  # 値を1つ右にずらす
            print(f"➡️ {arr} （{arr[position]} を右に移動）")
            position -= 1

        # 挿入すべき正しい位置に値を入れる
        arr[position + 1] = current_value
        print(f"✅ 挿入後: {arr}")

    return arr  # ソート済み配列を返す


# 【テストデータ】
unsorted_list = [5, 3, 8, 6, 2]
print("🔍 ソート前:", unsorted_list)

sorted_list = insertion_sort(unsorted_list)

print("\n✅ ソート後:", sorted_list)