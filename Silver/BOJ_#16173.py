N = int(input())
grid_map = []
for i in range(N):
    row = list(map(int, input().split()))
    grid_map.append(row)

def jelly_dfs_recursive(grid):
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0: # 그리드 초과시 False
            return False
        if grid[r][c] == -1: # 그리드 벗어나지 않고 도달 시 True
            return True
        step = grid[r][c] # 현재 칸 업데이트
        grid[r][c] = 0  # 방문처리
        return dfs(r + step, c) or dfs(r, c + step) # 현재 칸의 숫자만큼 점프(아래 또는 왼쪽으로)(두 방향 중 하나라도 True가 나오면 True)

    if dfs(0, 0):
        print("HaruHaru")
    else:
        print("Hing")

jelly_dfs_recursive(grid_map)