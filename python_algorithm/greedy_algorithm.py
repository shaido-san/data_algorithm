# 問題：ある金額を支払うのに必要な最小のコインの枚数を求めよ。
# コインの種類は、25円、10円、5円、1円

def min_coins(amount, coins):
    coins.sort(reverse=True) #コインを大きい順にソート
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# テスト
amount = 93
coins = [25, 10, 5, 1]
result = min_coins(amount, coins)
print(f"金額{amount}を払うのに必要なコイン: {result} (枚数: {len(result)})")
