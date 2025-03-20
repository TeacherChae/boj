N1, N2 = map(int, input().split())
ant_1 = list(input())
ant_2 = list(input())
T = int(input())
order = ant_1[::-1] + ant_2
for _ in range(T):
    for i in range(len(order)-1):
        if (order[i] in ant_1) and (order[i+1] in ant_2):
            order[i], order[i+1] = order[i+1], order[i]
            if order[i+1] == ant_1[0]:
                break
print(''.join(order))