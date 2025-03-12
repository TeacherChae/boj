n = int(input())
prime_num = []
for num in map(int, input().split()):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
    if count == 1:
        prime_num.append(num)
print(prime_num)