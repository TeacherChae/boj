N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            new_sum = cards[i] + cards[j] + cards[k]
            if new_sum <= M:
                sum = max(sum, new_sum)
print(sum)