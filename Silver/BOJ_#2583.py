import sys
from collections import deque

input = sys.stdin.readline

def cnt_plot(grid):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    r_lim = len(grid)
    c_lim = len(grid[0])

    def bfs(grid, y, x):
        queue = deque([[y,x]])
        grid[y][x] = True
        cnt = 1
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not(0 <= nr < r_lim and 0 <= nc < c_lim and grid[nr][nc] == False):
                    continue
                grid[nr][nc] = True
                queue.append([nr,nc])
                cnt += 1
        return cnt
    
    a_cnt = []
    p_cnt = 0
    for r in range(r_lim):
        for c in range(c_lim):
            if grid[r][c] == False:
                a_cnt.append(bfs(grid, r, c))
                p_cnt += 1
    return p_cnt, sorted(a_cnt)

M, N, K = map(int, input().split())
plot = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            plot[i][j] = True

p, a = cnt_plot(plot)
print(p)
print(*a)