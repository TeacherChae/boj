import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, order, start, cnt):
    visited[start] = True
    order[start] = cnt
    cnt += 1
    for adj in graph[start]:
        if not visited[adj]:
            cnt = dfs(graph, visited, order, adj, cnt)
    return cnt

N, M, R = map(int, input().split())
g = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for k in g:
    g[k].sort()

visited = [False] * (N + 1)
order = [0] * (N + 1)
dfs(g, visited, order, R, 1)

for i in range(1, N + 1):
    print(order[i])