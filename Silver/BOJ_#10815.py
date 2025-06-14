from collections import deque

N = int(input())
A = set(map(int, input().split()))

M = int(input())
M_int = map(int, input().split())
ans = deque()
for i in M_int:
    if i in A:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)