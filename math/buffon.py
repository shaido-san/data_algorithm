import random
import math

def buffon_needle(trials=1000000):
    hits = 0
    for _ in range(trials):
        theta = random.uniform(0, math.pi)
        d = random.uniform(0, 0.5)
        if d <= 0.5 * math.sin(theta):
            hits += 1
    return (2 * trials) / hits if hits > 0 else 0

print(buffon_needle())