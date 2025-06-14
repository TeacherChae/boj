def count_flips(sub):
    # sub: 8×8 리스트, 값은 0 또는 1
    flips_start0 = 0  # (0,0)=0인 패턴과 비교
    flips_start1 = 0  # (0,0)=1인 패턴과 비교
    for i in range(8):
        for j in range(8):
            expected0 = (i + j) % 2        # (0,0)=0 패턴
            expected1 = 1 - expected0      # (0,0)=1 패턴
            if sub[i][j] != expected0: flips_start0 += 1
            if sub[i][j] != expected1: flips_start1 += 1
    return min(flips_start0, flips_start1)

#1. 입력 받기
N, M = map(int, input().split())
bin_chess = {
    'B' : 0,
    'W' : 1
}
board = []
for _ in range(N):
    row = str(input())
    #1-1. 0, 1로 맵핑
    new_row = [bin_chess[row[i]] for i in range(M)]
    board.append(new_row)
#2. 8x8 구획
ans = float('inf')
for n in range(N - 7):
    for m in range(M - 7):
        # 8×8 부분 추출
        block = [row[m:m+8] for row in board[n:n+8]]
        ans = min(ans, count_flips(block))

print(ans)