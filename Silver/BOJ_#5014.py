import sys
from collections import deque

input = sys.stdin.readline


def bfs(f, s, g, u, d):
    v = [-1 for _ in range(f+1)] # 인덱스 0번은 더미
    v[s] = 0
    queue = deque([s])
    while queue:
        floor = queue.popleft()
        u_floor = floor + u
        d_floor = floor - d
        if 0 < u_floor <= f and v[u_floor] == -1:
            v[u_floor] = v[floor] + 1
            queue.append(u_floor)
        if 0 < d_floor <= f and v[d_floor] == -1:
            v[d_floor] = v[floor] + 1
            queue.append(d_floor)
    
    return v[g] if v[g] != -1 else "use the stairs"

F, S, G, U, D = map(int, input().split())

print(bfs(F, S, G, U, D))