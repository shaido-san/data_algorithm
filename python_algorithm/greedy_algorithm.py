# 問題：ある金額を支払うのに必要な最小のコインの枚数を求めよ。
# コインの種類は、25円、10円、5円、1円

def min_coins(amount, coins):
    coins.sort(reverse=True)    # コインを大きい順にソート
    result = []                 # 結果として必要なコインを保存するリスト
    for coin in coins:          # コインを順に処理する
        while amount >= coin:   # amountが現在のコインの額以上なら
            amount -= coin      # amountからそのコインの額を引く
            result.append(coin) # 結果リストにそのコインを追加
    return result               # 結果リストを返す

# テスト
amount = 867
coins = [25, 10, 5, 1]
result = min_coins(amount, coins)
print(f"金額{amount}を払うのに必要なコイン: {result} (枚数: {len(result)})")
