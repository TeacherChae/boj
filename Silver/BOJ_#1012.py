import sys
from collections import deque

input = sys.stdin.readline

def worm_cnt(graph, n, m):
    dr = [1, 0, -1 ,0]
    dc = [0, 1, 0, -1]

    def bfs(y, x):
        queue = deque([(y, x)])
        graph[y][x] = False
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and graph[nr][nc]:
                    graph[nr][nc] = False
                    queue.append((nr, nc))

    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x]:
                bfs(y, x)
                cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = True
    print(worm_cnt(farm, N, M))