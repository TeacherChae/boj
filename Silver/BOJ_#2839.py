N = int(input())
q_5 = N // 5 #5로 나눈 몫
q_3 = N // 3 #3으로 나눈 몫
res = []
for i in range(0, q_5+2):
    for j in range(0, q_3+2):
        if 5*i + 3*j == N:
            res.append(i+j)
if res:
    print(min(res))
else:
    print(-1)