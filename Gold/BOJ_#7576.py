from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
basket = []
rippen_tomatoes = []
fresh_tomatoes_cnt = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j, c in enumerate(row):
        if c == 1:
            rippen_tomatoes.append((i, j))
        elif c == 0:
            fresh_tomatoes_cnt += 1
    basket.append(row)
if fresh_tomatoes_cnt == 0:
    print(0)
if not rippen_tomatoes:
    print(-1)

def let_tomatoes_have_their_times(matrix, ripen):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    r_lim = len(matrix)
    c_lim = len(matrix[0])
    def bfs(matrix, ripen):
        visited = set()
        queue = deque()
        for coord in ripen:
            visited.add(coord)
            queue.append(coord)
        count = 0
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if (nr, nc) not in visited and (0 <= nr < r_lim and 0 <= nc < c_lim):
                    if matrix[nr][nc] == 0: 
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        matrix[nr][nc] = 1
                else:
                    continue
            count += 1
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    return -1
        return count // len(ripen)
    
    return bfs(matrix, ripen)

print(let_tomatoes_have_their_times(basket, rippen_tomatoes))
