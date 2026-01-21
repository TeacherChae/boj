import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    dr = [2, 1, -1, -2, -2, -1, 1, 2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([[r1, c1]])
    
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if not(0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0):
                continue
            
            queue.append([nr, nc])
            visited[nr][nc] = visited[r][c] + 1
            
            if nr == r2 and nc == c2:
                return visited[nr][nc]

T = int(input())
for _ in range(T):
    I = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    print(bfs(I, sr, sc, er, ec))