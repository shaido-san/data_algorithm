def logistic_map(r, x=0.5, steps=100):
    print(f"初期値 x = {x}, r = {r}")
    for i in range(steps):
        x = r * x * (1 - x)
        print(f"ステップ {i+1:3}: x = {x:.6f}")

logistic_map(r=3.7)