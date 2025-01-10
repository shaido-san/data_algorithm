# 問題：線分の集合が与えられて時、お互いに重ならない
# 最大の線分を選べ。

def interval_scheduling(intervals):
    # 区間を終了時刻でソート
    intervals.sort(key=lambda x: x[1])
    selected = []
    current_end = float('-inf')

    for start, end in intervals:
        if start >= current_end:
            selected.append((start, end))
            current_end = end
    
    return selected

# テスト
intervals = [(1, 2), (2, 3), (3, 4), (1, 3),(2, 5), (4, 6)]
result = interval_scheduling(intervals)
print(f"選ばれた区間：{result}")