import random

def monte_carlo_pi(n=10000):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return (inside / n) * 4

print(monte_carlo_pi())