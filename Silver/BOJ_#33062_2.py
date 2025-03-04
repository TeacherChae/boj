# T : 체인 반올림과 표준 반올림이 달라지는 임계값

# ex) N = 51 : D = 2, L = 10, diff_previous_count = 0
# T = 45
# 45 = 50 - 5
# diff_current_count = 5
# diff_count_total = diff_previous_count + diff_current_count = 5

# ex) N = 501 : D = 3, L = 100, diff_previous_count = 5
# T = 445
# 445 = 500 - 55
# diff_current_count = 55
# diff_count_total = diff_current_count + diff_previous_count = 55 + 5

# ex) N = 5001 : D = 4, L = 1000
# T = 4445
# 4445 = 5000 - 500 - 50 - 5
# diff_current_count = 555
# diff_count_total = diff_current_count + diff_previous_count = 555 + 55 + 5

# ex) N = 50001 : D = 5, L = 10000
# T = 44445
# 44445 = 50000 - 5000 - 500 - 50 - 5
# diff_current_count = 5555
# diff_count_total = diff_current_count + diff_previous_count = 5555 + 555 + 55 + 5


T = int(input())
for _ in range(T):
    N_line = input()
    N = int(N_line)
    ans = 0
    P = 2
    while True:
        base = 10 ** (P - 1)
        L = 4 * base
        if L > N:
            break
        U_candidate = 5 * base - 1
        curr_range = min(N, U_candidate) - L + 1
        T = (4 * base + 5) // 9
        if curr_range > T:
            ans += (curr_range - T)
        P += 1
    print(ans)