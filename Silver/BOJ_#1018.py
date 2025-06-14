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
'''
ex. board[i][j]
'''
count_candidate = []
for n in range(N-7):
    for m in range(M-7):
        chess_board = []
        count = 0
        for line in board[n:n+8]:
            candidate = line[m:m+8]
            chess_board.append(candidate)
        for i in range(7):
            for j in range(7):
                if chess_board[i][j] == chess_board[i][j+1]:
                    chess_board[i][j+1] = 1 - chess_board[i][j+1]
                    count += 1
                if chess_board[i][j] == chess_board[i+1][j]:
                    chess_board[i+1][j] = 1 - chess_board[i+1][j]
                    count += 1
        if chess_board[6][6] != chess_board[7][7]:
            count += 1
        count_candidate.append(count)
print(min(count_candidate))











#2. 8x8 고르기
'''
i~i+8:
i += 1
'''
# for i in range(N-7):
#     candidate = board[i:i+8]
#     for j in range(M-7):
#         for line in candidate:
#             r = line[j:j+8]
#             next_r = board[i+1][j:j+8]
#             print(f'{i}번째 줄: {r}, {i+1}번째 줄: {next_r}')
            #3. 하나씩 접근하기
            # #3. BW검증하기
            # for k in range(7):

            # #     if j == M-8:
            # #         break
            #     if r[k] == 'W'
            #         #3-1. c[k]가 c[k+1]와 같을 때
            #         if r[k] == r[k+1]:
            #             r[k+1] = 'B'
            #             count += 1
            #         #3-2. r[j+1:j+9][k]와 같을 때
            #         if r[k] == line[j+1:j+9][k]:
            #             line[j+1:j+9][k] = 'B'
            #             count += 1
            #     else:
            #         if r[k] == r[k+1]:
            #             r[k+1] = 'W'
            #             count += 1
            #         if r[k] == line[j+1:j+9][k]:
            #             line[j+1:j+9][k] = 'W'
            #             count += 1