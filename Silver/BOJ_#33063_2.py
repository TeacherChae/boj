import sys
input  = sys.stdin.readline
write  = sys.stdout.write

N, Q = map(int, input().split())

# N×N 개의 라인을 각각 1차원 인덱스로 flatten
row_cnt = [0] * (N * N)   # (z,y)마다 x축 방향 깎인 칸 수
col_cnt = [0] * (N * N)   # (z,x)마다 y축
pil_cnt = [0] * (N * N)   # (y,x)마다 z축

total = 0
ans = []  # 문자열로 누적

for _ in range(Q):
    x, y, z = map(int, input().split())

    idx1 = z * N + y
    row_cnt[idx1] += 1
    if row_cnt[idx1] == N:
        total += 1

    idx2 = z * N + x
    col_cnt[idx2] += 1
    if col_cnt[idx2] == N:
        total += 1

    idx3 = y * N + x
    pil_cnt[idx3] += 1
    if pil_cnt[idx3] == N:
        total += 1

    ans.append(str(total))

# 한 번에 출력
write("\n".join(ans))

