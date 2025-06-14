N, K = map(int, input().split())
days = list(map(int, input().split()))

# 두 날짜 사이로만 일단 계산
def greedy_diff(n, m, K):
    indiv = 1 + K
    series = (m-n)
    return min(indiv, series)

greedy = 1+K
for i in range(N-1):
    greedy += greedy_diff(days[i], days[i+1], K)
print(greedy)