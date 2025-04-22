import random

def self_avoiding_walk(size=21, max_steps=100):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    x = y = size // 2
    grid[y][x] = 'S'  # スタート地点

    path = [(x, y)]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for _ in range(max_steps):
        random.shuffle(directions)
        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == '.':
                x, y = nx, ny
                grid[y][x] = '*'
                path.append((x, y))
                moved = True
                break
        if not moved:
            grid[y][x] = 'X'  # 行き止まり
            break

    # グリッド出力
    for row in grid:
        print(''.join(row))
    print(f"\n歩数: {len(path)}")

self_avoiding_walk()