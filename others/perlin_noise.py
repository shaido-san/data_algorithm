import random
import matplotlib.pyplot as plt
import numpy as np

def lerp(a, b, x):
    return a + x * (b - a)

def fade(t):
    return 6*t**5 - 15*t**4 + 10*t**3

def grad(hash, x):
    return (hash & 1) * 2 - 1  # 1 or -1

def perlin(x):
    x0 = int(x) & 255
    x1 = (x0 + 1) & 255
    u = fade(x - int(x))

    g0 = grad(p[x0], x - int(x))
    g1 = grad(p[x1], x - int(x) - 1)

    return lerp(g0, g1, u)

# パーマネーションテーブル（ランダム順）
p = list(range(256))
random.shuffle(p)
p = p * 2

# 可視化
xs = np.linspace(0, 50, 500)
ys = [perlin(x * 0.1) for x in xs]

plt.plot(xs, ys)
plt.title("Perlin Noise (1D)")
plt.grid()
plt.show()