N, K = map(int, input().split())
factor = [i for i in range(1, N+1) if N % i == 0]
if len(factor) < K:
    print(0)
else:
    print(factor[K-1])