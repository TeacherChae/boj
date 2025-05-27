def rotate(s):
    return [list(reversed(col)) for col in zip(*s)]

def check_valid(c:list, s:list):
    s_size = len(s)
    for i in range(s_size):
        for j in range(s_size):
            if s[i][j] == '*' and c[i][j] == '.':            
                return False
    else:
        return True

T = int(input())
for _ in range(T):
    input()
    N = int(input())
    canvas = [list(input().strip()) for _ in range(N)]
    K = int(input())
    stamp  = [list(input().strip()) for _ in range(K)]
    print(canvas, stamp)

    # 1) 회전본 만들기
    stamps = [stamp]
    for _ in range(3):
        stamps.append(rotate(stamps[-1]))

    # 2) 커버 행렬
    covered = [[False]*N for _ in range(N)]

    # 3) 모든 위치에서 찍기 시뮬레이션
    for s in stamps:
        for r in range(N-K+1):
            for c in range(N-K+1):
                if check_valid(
                    [row[c:c+K] for row in canvas[r:r+K]],
                    s
                ):
                    for i in range(K):
                        for j in range(K):
                            if s[i][j] == '*':
                                covered[r+i][c+j] = True

    # 4) 최종 판정
    ok = all(
        covered[i][j] or canvas[i][j]=='.'
        for i in range(N) for j in range(N)
    )
    print("YES" if ok else "NO")


# canvas, new_canvas를 비교하는 것?
# 도장의 시작점을 한칸씩 옮길 때마다 90도씩 4번 돌리면서 체크. <- 모든 경우의 수를 체크

# . .
# . *
# canvas가 이런데
# . *
# * *
# stamp가 이런 경우

# if canvas의 *개수가 stamp의 *개수보다 적을 경우: NO
# else:

# * . *
# . * .
# * . *
# canvas가 이런데
# . . .
# . * .
# . . .
# stamp가 이런 경우


# 모든 경우의 수를 체크하고도 new_canvas가 canvas랑 다르면 NO



#1. 각 좌표 별로 체크한다.
# 뭘 체크하는지?
# 

#1-1. canvas가 .인데 stamp가 *이면 제외하고 90도 돌린다.
#1-2. 나머지의 경우는 new_canvas에 반영한다.



# for _ in range(4):
#     if check_valid(s,c):
#         ??
#     else:
#         pass
#     rotate(s)

# while True:
    


# T = int(input())

# for i in range(T):
#     space = input()
#     N = int(input())
#     n = [input() for _ in range(N)]
#     canvas = []
#     for item in n:
#         l = [*item]
#         canvas.append(l)
#     K = int(input())
#     k = [input() for _ in range(K)]
#     stamp = []
#     for item in k:
#         l = [*item]
#         stamp.append(l)
#     print(canvas, stamp)
    