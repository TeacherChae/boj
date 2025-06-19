import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(graph, start):
    visited = set()
    visited.add(start)
    order = defaultdict(int)
    cnt = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order[node] = cnt
        cnt += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return order

N, M, R = map(int, input().split())
g = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for k in g:
    g[k].sort(reverse=True)

v = bfs(g, R)
for i in range(1, N+1):
    print(v[i])
