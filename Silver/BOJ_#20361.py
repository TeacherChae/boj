N, X, K = map(int, input().split())
N = [num + 1 for num in range(N)]
curr = N[X-1]
for i in range(K):
    a, b = map(int, input().split())
    N[a-1], N[b-1] = N[b-1], N[a-1]
print(N.index(curr) + 1)