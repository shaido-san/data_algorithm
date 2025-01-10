# 問題：各アクティビティビティの開始時刻と終了時刻が与えられた時、
# お互いに重ならない最大数のアクティビティを選んでください。

def activity_selection(activities):
    # アクティビティを終了時刻でソート
    # 終了時刻が早い順に並べることで、選択肢を増やす戦略
    activities.sort(key=lambda x: x[1])
    
    # 重ならないアクティビティを格納するリストを初期化
    selected = []
    
    # 最初のアクティビティの終了時刻は0と仮定
    current_end = 0

    # 各アクティビティを確認するループ
    for start, end in activities:
        # アクティビティの開始時刻が、最後に選ばれたアクティビティの終了時刻より後の場合
        if start >= current_end:
            # アクティビティを選択リストに追加
            selected.append((start, end))
            # 現在の終了時刻をこのアクティビティの終了時刻に更新
            current_end = end
    
    # 重ならないアクティビティのリストを返す
    return selected

# テストデータ
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8)]

# 関数を実行して、重ならないアクティビティを選択
result = activity_selection(activities)

# 結果を表示
print(f"選ばれたアクティビティ: {result}")