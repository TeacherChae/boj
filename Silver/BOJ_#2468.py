import sys
from collections import deque

input = sys.stdin.readline
def get_area_cnt(graph, h):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    def bfs(y, x, h):
        visited[y][x] = True
        queue = deque([[y,x]])
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False and graph[nr][nc] > h: # 방문한 적 없고 침수 안 될 시
                    visited[nr][nc] = True # 방문 처리
                    queue.append([nr, nc])
    a_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] > h:
                bfs(i, j, h)
                a_cnt += 1
    return a_cnt

N = int(input())
matrix = []
number = set()
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    for r in row:
        number.add(r)
max_cnt = 0
for height in range(max(number)):
    max_cnt = max(max_cnt, get_area_cnt(matrix, height))
print(max_cnt)