M = int(input())
N = int(input())
prime_nums = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** (1/2) + 1)):
        if num % i == 0:
            return False
    return True

for num in range(M, N + 1):
    if is_prime(num):
        prime_nums.append(num)

if not prime_nums:
    print(-1)
else:
    print(sum(prime_nums))
    print(min(prime_nums))