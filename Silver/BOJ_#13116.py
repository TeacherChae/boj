T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    print(a * 10)