N = int(input())
const = []
for i in range(1, N):
    str_N = str(i)
    str_sum = 0
    for j in str_N:
        num = int(j)
        str_sum += num
    res = i + str_sum    
    if res == N:
        const.append(i)
if const:
    print(min(const))
else:
    print(0)
