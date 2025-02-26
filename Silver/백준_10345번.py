# count = 0
# while True:
#     W, N = map(int, input().split())
#     if W == N == 0:
#         break
#     S = []
#     C = []
#     for i in range(N):
#         s, c = input().split()
#         S.append(s)
#         C.append(int(c))
#     # 줄이 나뉘든 나뉘지 않든 각 단어 별 폰트 크기와 폭은 정해져있다.
#     lens = [len(item) for item in S]
#     pts = [8 + int(((40 * (item - 4)) / (max(C) -4))) for item in C] # 단어 별 폰트
#     word_width = [int((9 / 16 * pt * len)) for pt, len in zip(pts, lens)] # 단어 별 폭

#     width_written = 0 # word_width + 10의 누적
#     height = [] # 한 줄에 쓰인 각 단어의 높이
#     max_height = [] # 한 줄에 쓰인 최대 단어 높이
#     for i in range(N): # 단어 수만큼 반복
#         width_written += word_width[i] + 10 
#         height.append(pts[i])
#         if width_written > W + 10: # 한 줄에 다 못 들어가면
#             height = height[:-1] # 넘어가기 전 단어까지만 저장
#             max_height.append(max(height)) # 한 줄에 쓰인 최대 단어 높이
#             width_written = word_width[i] + 10 # 넘어간 단어로 초기화
#             height = [pts[i]] # 넘어간 단어로 초기화
#     max_height.append(max(height)) # 마지막 줄까지 추가
#     p = sum(max_height)
#     count += 1
#     print(f'CLOUD{count}: {p}')


# def calc_cloud_height(W, S, C):
#     """
#     폭(W), 단어 목록(S), 중요도 목록(C)을 입력받아
#     구름(CLOUD)의 높이(p)를 계산해 반환하는 함수
#     """
#     # 단어 길이, 폰트 크기, 단어 폭 계산
#     lengths = [len(word) for word in S]
#     max_c = max(C)

#     # pts: 각 단어의 폰트 크기
#     #  - 예시 공식: 8 + int(((40 * (c - 4)) / (max_c - 4)))
#     #    단, max_c가 4와 같을 경우 나눗셈 에러가 생길 수 있으므로 주의(필요시 예외처리)
#     pts = [8 + int((40 * (c - 4)) / (max_c - 4)) for c in C]

#     # word_widths: 각 단어 출력 시 폭
#     #  - 예시 공식: int((9 / 16) * pt * 단어길이)
#     word_widths = [
#         int((9.0 / 16.0) * pt * length)
#         for pt, length in zip(pts, lengths)
#     ]

#     width_written = 0    # 현재 줄 누적 폭(단어 폭 + 공백 폭)
#     line_heights = []    # 현재 줄에 들어간 단어들의 높이
#     max_heights = []     # 각 줄의 최대 높이를 모아둠

#     for i in range(len(S)):
#         # 단어 폭 + 공백(10)만큼 누적
#         width_written += word_widths[i] + 10

#         # 현재 단어의 폰트 크기(= 높이) 추가
#         line_heights.append(pts[i])

#         # 만약 줄의 폭을 넘었다면, (이번 단어를 새 줄로 빼야 함)
#         if width_written > W + 10:
#             # 초과한 단어(i번째)는 이전 줄에서 제외해야 하므로 pop
#             line_heights.pop()

#             # 이전 줄의 최대 높이 기록
#             max_heights.append(max(line_heights))

#             # 다음 줄 시작 처리
#             width_written = word_widths[i] + 10
#             line_heights = [pts[i]]

#     # 마지막 줄도 최대 높이를 기록
#     if line_heights:
#         max_heights.append(max(line_heights))

#     # 전체 높이 = 각 줄의 최대 높이 합
#     return sum(max_heights)


# def main():
#     n = 1  # CLOUD 번호 (회차)
#     while True:
#         # W, N 입력
#         W, N = map(int, input().split())
#         # 0 0 이면 종료
#         if W == 0 and N == 0:
#             break

#         # 단어/중요도 입력받기
#         S = []
#         C = []
#         for _ in range(N):
#             s, c = input().split()
#             S.append(s)
#             C.append(int(c))

#         # 구름 높이 계산
#         p = calc_cloud_height(W, S, C)

#         # 결과 출력
#         print(f'CLOUD {n}: {p}')

#         # 다음 회차 번호 증가
#         n += 1


# if __name__ == "__main__":
#     main()
def operate_ceil(x: float) -> int:
    """
    x보다 작지 않은 정수 중 가장 작은 정수를 반환
    """
    ix = int(x)
    return ix if x <= ix else ix + 1

cloud_number = 1
while True:
    try:
        line = input().strip()
    except EOFError:
        # EOF(입력 끝)에 도달하면 종료
        break
    
    # 빈 줄이면 건너뛰고 다음 반복
    if not line:
        continue
    
    # W, N 파싱
    W, N = map(int, line.split())
    
    # W==0 또는 N==0이면 입력 종료
    if W == 0 or N == 0:
        break
    
    # N개의 (단어, 빈도수) 읽기
    words = []
    counts = []
    for _ in range(N):
        line2 = input().strip()
        s, c = line2.split()
        c = int(c)
        words.append(s)
        counts.append(c)
    
    # 최댓값 c_max
    c_max = max(counts)

    fonts = []
    widths = []
    for i in range(N):
        c_w = counts[i]
        # P = 8 + ⌈ 40*(c_w - 4)/(c_max - 4) ⌉
        P = 8 + operate_ceil(40 * (c_w - 4) / (c_max - 4))
        
        # width = ⌈ (9/16) * (단어길이) * P ⌉
        w = operate_ceil((9/16) * len(words[i]) * P)
        
        fonts.append(P)
        widths.append(w)
    
    # 줄 단위로 배치
    total_height = 0
    row_width = 0
    row_max_font = 0
    
    for i in range(N):
        word_width = widths[i]
        font_size = fonts[i]
        
        if row_width == 0:
            # 새 줄 시작
            row_width = word_width
            row_max_font = font_size
        else:
            # 다음 단어를 넣을 수 있는지 확인(공백 10pt 포함)
            if row_width + 10 + word_width <= W:
                row_width += 10 + word_width
                row_max_font = max(row_max_font, font_size)
            else:
                # 현재 줄의 최대 폰트 크기를 높이에 반영
                total_height += row_max_font
                # 새 줄 시작
                row_width = word_width
                row_max_font = font_size
    
    # 마지막 줄 높이 추가
    if row_width > 0:
        total_height += row_max_font
    
    print(f"CLOUD {cloud_number}: {total_height}")
    cloud_number += 1