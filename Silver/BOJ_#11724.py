def dfs_stack(graph, start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)
    
    return visited

import sys
sys.setrecursionlimit(10**6)

def dfs_recursive(graph, node, visited):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

N, M = map(int, input().split())

# 모든 정점 초기화
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
cnt = 0

for node in range(1, N + 1):
    if node not in visited:
        dfs_recursive(graph, node, visited)
        cnt += 1

print(cnt)

#----------------------------------------------------#

def dfs_stack(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # 인접 노드를 스택에 추가 (내림차순 정렬하면 재귀와 순서 맞춤 가능)
            stack.extend(graph[node])


N, M = map(int, input().split())

# 모든 정점 초기화
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
cnt = 0

for node in range(1, N + 1):
    if node not in visited:
        dfs_stack(graph, node, visited)
        cnt += 1

print(cnt)

#----------------------------------------------------#

import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]  # 자기 자신이 부모

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    union(u, v)

roots = set(find(i) for i in range(1, N + 1))
print(len(roots))

#----------------------------------------------------#

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, graph, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()
cnt = 0

for node in range(1, N + 1):
    if node not in visited:
        bfs(node, graph, visited)
        cnt += 1

print(cnt)