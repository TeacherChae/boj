N = int(input().strip())
commands = input().strip()

# 방향을 정수로 표현해 보자.
# 0: 남쪽, 1: 서쪽, 2: 북쪽, 3: 동쪽
dir_idx = 0

# 각 방향별 (dr, dc) 정의
# 남쪽(0) -> (1, 0), 서쪽(1) -> (0, -1),
# 북쪽(2) -> (-1, 0), 동쪽(3) -> (0, 1)
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

# 시작 위치 (r, c) = (0, 0)
r, c = 0, 0

# 방문 좌표들을 저장할 리스트 (또는 세트)
visited = [(r, c)]

# 방문 좌표의 최소·최대 r, c값
min_r, max_r = 0, 0
min_c, max_c = 0, 0

# 명령어 처리
for cmd in commands:
    if cmd == 'R':
        # 오른쪽 회전: 방향 인덱스 +1
        dir_idx = (dir_idx + 1) % 4
    elif cmd == 'L':
        # 왼쪽 회전: 방향 인덱스 -1
        dir_idx = (dir_idx - 1) % 4
    elif cmd == 'F':
        # 전진: 현재 바라보는 방향대로 (r, c) 이동
        r += dr[dir_idx]
        c += dc[dir_idx]
        visited.append((r, c))

        # 이동 후, min/max 갱신
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    # 그 외 다른 문자가 들어올 일은 없다고 가정

# 이제 (min_r, max_r), (min_c, max_c) 범위를 이용해
# 미로(2차원 배열)를 생성
height = max_r - min_r + 1
width = max_c - min_c + 1

# 초기에는 전부 '#'으로 채움
maze = [['#'] * width for _ in range(height)]

# 방문했던 좌표는 '.'으로 표시
for (rr, cc) in visited:
    maze[rr - min_r][cc - min_c] = '.'

# 최종 출력
for row in maze:
    print(''.join(row))