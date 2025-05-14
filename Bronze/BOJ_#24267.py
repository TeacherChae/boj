n = int(input())
sum = 0
for k in range(1, n-1):
    sum += (n-1-k) * (n-2-k) // 2
print(sum)
print(3)