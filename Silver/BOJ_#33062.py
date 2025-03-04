T = int(input())
for _ in range(T):
    N = int(inpu())

    answer = 0
    lo, hi = 45, 49
    while lo <= N:
        answer += min(hi, N) - lo + 1
        lo = lo * 10 - 5
        hi = hi * 10 + 9
    print(answer)