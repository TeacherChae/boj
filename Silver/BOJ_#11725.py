from collections import deque

def dfs_parent(start, graph, parent):
    visited = set()
    stack = deque([start])
    visited.add(start)
    while stack:
        top = stack.pop()
        for node in graph[top]:
            if node not in visited:
                parent[node] = top
                visited.add(node)
                stack.append(node)

N = int(input())
g = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

p = {1: None}
dfs_parent(1, g, p)

for j in range(2, N+1):
    print(p[j])
