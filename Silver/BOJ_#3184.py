R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs_stack(x, y, mark_char):
    stack = [(x, y)]
    region = []

    while stack:
        cx, cy = stack.pop()
        if not (0 <= cx < R and 0 <= cy < C):
            continue
        if grid[cx][cy] == '#' or grid[cx][cy] == mark_char:
            continue

        region.append(grid[cx][cy])
        grid[cx][cy] = mark_char

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            stack.append((nx, ny))

    return region

for i in range(R):
    for j in [0, C - 1]:
        if grid[i][j] != '#' and grid[i][j] != 'X':
            dfs_stack(i, j, 'X')
for j in range(C):
    for i in [0, R - 1]:
        if grid[i][j] != '#' and grid[i][j] != 'X':
            dfs_stack(i, j, 'X')

total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] not in ['#', 'X']:
            region = dfs_stack(i, j, 'X')
            sheep = region.count('o')
            wolf = region.count('v')
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)