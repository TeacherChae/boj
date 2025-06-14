N = int(input())
commands = input()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 2

x, y = 0, 0
visited = [(x, y)]

max_x, min_x = 0, 0
max_y, min_y = 0, 0

for cmd in commands:
    if cmd == 'R':
        direction = (direction + 1) % 4
    elif cmd == 'L':
        direction = (direction - 1) % 4
    else:  # 'F'
        x += dx[direction]
        y += dy[direction]
        visited.append((x, y))
        
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

h = max_y - min_y + 1
w = max_x - min_x + 1
matrix = [['#'] * w for _ in range(h)]

for nx, ny in visited:
    real_x = nx - min_x
    real_y = ny - min_y
    matrix[real_y][real_x] = '.'

for row in matrix:
    print(''.join(row))
