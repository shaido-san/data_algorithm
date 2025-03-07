def binary_search(arr, target):
    """
    二分探索（Binary Search）
    - ソートされた配列からターゲットの値を探索し、そのインデックスを返す。
    - 見つからなかった場合は -1 を返す。

    探索の流れ:
    1. 配列の中央の値を確認
    2. ターゲットが中央より大きければ右半分、小さければ左半分を探索
    3. 見つかるまで範囲を狭めていく（O(log N) の計算量）
    """

    # 1. 探索範囲の初期の境界を設定（左端: left, 右端: right）
    left, right = 0, len(arr) - 1

    # 2. 探索範囲がある限り繰り返す
    while left <= right:
        # 3. 中央のインデックスを求める
        mid = (left + right) // 2

        # 4. 現在の探索範囲を表示（デバッグ用）
        print(f"探索範囲: arr[{left}:{right + 1}] -> {arr[left:right+1]} (mid={mid}, 値={arr[mid]})")

        # 5. 中央の値がターゲットならインデックスを返す
        if arr[mid] == target:
            return mid

        # 6. ターゲットが中央より大きい場合（右半分を探索）
        elif arr[mid] < target:
            left = mid + 1  # 左端を更新（右側へ）

        # 7. ターゲットが中央より小さい場合（左半分を探索）
        else:
            right = mid - 1  # 右端を更新（左側へ）

    # 8. 見つからなかった場合 -1 を返す
    return -1


# 【テスト用の配列】
# 二分探索は「ソートされた配列」でのみ機能する
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# 【検索テスト】
targets = [15, 7, 4, 21, 1]  # 検索するターゲットのリスト

for target in targets:
    print(f"\n🔍 ターゲット {target} を検索中...")
    index = binary_search(sorted_numbers, target)
    
    if index != -1:
        print(f"✅ ターゲット {target} はインデックス {index} にあります。\n")
    else:
        print(f"❌ ターゲット {target} は見つかりませんでした。\n")