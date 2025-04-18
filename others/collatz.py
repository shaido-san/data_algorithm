def collatz(n):
    print(f"初期値: {n}")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
    print("終了: 1 に到達")

collatz(27)