def solve_maze(maze, start, end):
    from collections import deque
    queue = deque([start])
    visited = set()
    while queue:
        pos = queue.popleft()
        if pos == end:
            return True
        if pos in visited:
            continue
        visited.add(pos)
        x, y = pos
        for dx, dy in [(-1,0), (1,0), (0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                queue.append((nx, ny))
    return False

maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]
start = (0, 0)
end = (3, 3)

print(solve_maze(maze, start, end)) 