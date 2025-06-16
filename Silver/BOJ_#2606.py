import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(graph, start):
    visited = [start]
    stack = [start]
    while stack:
        top = stack.pop()
        for node in graph[top]:
            if node not in visited:
                visited.append(node)
                stack.append(node)
    return visited

n = int(input())
m = int(input())

g = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

v = dfs(g, 1)
print(len(v)-1)