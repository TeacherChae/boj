N = int(input())
C = list(map(int, input().split()))
c= list(set(C))
tuition_sum = []
for i in c:
    count = 0
    for j in C:
        if j >= i:
            count += i
        else:
            continue
    pair = (count, i)
    tuition_sum.append(pair)
tuition_sum.sort(key=lambda x: (-x[0], x[1]))
best_revenue, best_tuition = tuition_sum[0]
print(best_revenue, best_tuition)
