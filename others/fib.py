def fib(n):
    # 計算を表示
    print("n =", n, "の計算を開始します")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

val = fib(4)
print(val)