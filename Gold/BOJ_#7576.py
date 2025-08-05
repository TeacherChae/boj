import sys
from collections import deque
input = sys.stdin.readline

def bfs(matrix, starts, N, M):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    queue = deque()
    for r, c in starts:
        queue.append((r, c, 0))  # (행, 열, 날짜)

    max_day = 0
    while queue:
        r, c, day = queue.popleft()
        max_day = max(max_day, day)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                matrix[nr][nc] = 1  # 익히기
                queue.append((nr, nc, day + 1))

    # 모든 토마토가 익었는지 확인
    for row in matrix:
        if 0 in row:
            return -1
    return max_day

M, N = map(int, input().split())
matrix = []
ripen_tomatoes = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            ripen_tomatoes.append((i, j))
    matrix.append(row)

print(bfs(matrix, ripen_tomatoes, N, M))
