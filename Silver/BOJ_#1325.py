'''
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3
예제 출력 1 
1 2
'''
import sys
from collections import deque, defaultdict

def dfs(graph, start):
    visited = set([start])
    stack = [start]
    cnt = 0
    while stack:
        top = stack.pop()
        for child in graph[top]:
            if child not in visited:
                visited.add(child)
                stack.append(child)
                cnt += 1
    return cnt


input = sys.stdin.readline

N, M = map(int, input().split())
g = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    g[b].append(a)
answer = [0] * (N + 1)
max_v = 0
for i in list(g):
    n = dfs(g, i)
    answer[i] = n

for i in list(g):
    if answer[i] == max_v:
        print(i, end=' ')

# -------------------------------------------- #
import sys
sys.setrecursionlimit(1000000)

def input_data():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    # reversed graph: b -> a
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(next(it)); b = int(next(it))
        g[b].append(a)
    return N, M, g

def tarjan(N, g):
    dfn = [0]*(N+1)
    low = [0]*(N+1)
    onstack = [False]*(N+1)
    stk = []
    idx = 1
    comp_id = [0]*(N+1)
    comp_cnt = 0

    def dfs(u):
        nonlocal idx, comp_cnt
        dfn[u] = low[u] = idx; idx += 1
        stk.append(u); onstack[u] = True
        for v in g[u]:
            if dfn[v] == 0:
                dfs(v)
                low[u] = low[u] if low[u] < low[v] else low[v]
            elif onstack[v]:
                low[u] = low[u] if low[u] < dfn[v] else dfn[v]
        # head of SCC
        if low[u] == dfn[u]:
            while True:
                w = stk.pop()
                onstack[w] = False
                comp_id[w] = comp_cnt
                if w == u: break
            comp_cnt += 1

    for u in range(1, N+1):
        if dfn[u] == 0:
            dfs(u)

    return comp_cnt, comp_id

def solve():
    N, M, g = input_data()

    # 1) SCC 압축
    comp_cnt, comp_id = tarjan(N, g)

    # 2) 각 컴포넌트에 속한 원래 노드들의 수집
    comp_nodes = [[] for _ in range(comp_cnt)]
    for u in range(1, N+1):
        comp_nodes[comp_id[u]].append(u)

    # 3) 축소 DAG 구성
    comp_graph = [[] for _ in range(comp_cnt)]
    indeg = [0]*comp_cnt
    seen_edge = set()
    for u in range(1, N+1):
        cu = comp_id[u]
        for v in g[u]:
            cv = comp_id[v]
            if cu != cv:
                # 중복 간선 방지
                if (cu,cv) not in seen_edge:
                    seen_edge.add((cu,cv))
                    comp_graph[cu].append(cv)
                    indeg[cv] += 1

    # 4) 위상 정렬 (Kahn)
    from collections import deque
    dq = deque([i for i in range(comp_cnt) if indeg[i]==0])
    topo = []
    while dq:
        u = dq.popleft()
        topo.append(u)
        for v in comp_graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)

    # 5) 각 컴포넌트별 비트마스크 초기화
    #    노드 ID 1~N 을 0~N-1 비트로 사용
    bits = [0]*comp_cnt
    for c in range(comp_cnt):
        mask = 0
        for u in comp_nodes[c]:
            mask |= 1 << (u-1)
        bits[c] = mask

    # 6) 위상 역순 DP: 상위 컴포넌트 ← 하위 컴포넌트 OR
    for u in reversed(topo):
        bm_u = bits[u]
        for v in comp_graph[u]:
            bm_u |= bits[v]
        bits[u] = bm_u

    # 7) 각 원래 노드의 해킹 가능 개수 계산
    #    popcount(bits[comp_id[u]]) - 1
    #    (자기 자신 제외)
    comp_count_cache = [b.bit_count() for b in bits]
    counts = [0]*(N+1)
    mx = 0
    for u in range(1, N+1):
        c = comp_count_cache[comp_id[u]] - 1
        counts[u] = c
        if c > mx:
            mx = c

    # 8) 최대값인 노드들 오름차순 출력
    out = [str(u) for u in range(1, N+1) if counts[u] == mx]
    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    solve()