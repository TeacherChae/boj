N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))
res = []
for num in M_card:
    res.append(N_card.count(num))
print(*res)