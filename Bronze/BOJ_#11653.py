N = int(input())

if N != 1:
    factor = 2
    while factor * factor <= N:
        while N % factor == 0:
            print(factor)
            N //= factor
        factor += 1
    if N > 1:
        print(N)