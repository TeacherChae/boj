# from itertools import product

# def beats(die1, die2):
#     """두 주사위 간의 승부 판별: die1이 die2보다 이겼으면 True, 아니면 False."""
#     win1 = win2 = 0
#     for x in die1:
#         for y in die2:
#             if x > y:
#                 win1 += 1
#             elif x < y:
#                 win2 += 1
#     return win1 > win2

# def is_c_possible(a, b):
#     # a와 b 중 누가 이기는지 결정
#     if beats(a, b):
#         strong, weak = a, b  # strong: 더 강한 주사위, weak: 더 약한 주사위
#     elif beats(b, a):
#         strong, weak = b, a
#     else:
#         # a와 b가 서로 비긴다면 non-transitive 관계를 만들기 어렵다고 가정
#         return False

#     # 후보 C: 1부터 10까지 숫자 중 4개를 할당하는 모든 경우 (10^4 = 10000가지)
#     # 조건: C는 강한 주사위를 이겨야 하고(즉, beats(C, strong)==True),
#     #      약한 주사위에게는 져야 함(즉, weak가 C를 이겨야 하므로 beats(weak, C)==True).
#     for candidate in product(range(1, 11), repeat=4):
#         c = list(candidate)
#         if beats(c, strong) and beats(weak, c):
#             return True  # 조건을 만족하는 C를 찾으면 바로 True 반환
#     return False

# # 입력 처리
# T = int(input().strip())
# for _ in range(T):
#     numbers = list(map(int, input().split()))
#     a = numbers[:4]
#     b = numbers[4:]
#     print('yes' if is_c_possible(a, b) else 'no')

from itertools import combinations_with_replacement
import sys

def beats(die1, die2):
    """die1이 die2를 이기면 True, 아니면 False를 반환 (16번 비교)"""
    win1 = win2 = 0
    for x in die1:
        for y in die2:
            if x > y:
                win1 += 1
            elif x < y:
                win2 += 1
    return win1 > win2

def candidate_possible(strong, weak, candidate):
    """
    candidate가 강한 주사위(strong)를 이기고, 약한 주사위(weak)에게 지는지 확인.
    candidate와 강한 주사위의 면 4×4 비교에서 candidate가 이기는 횟수가 9 이상이어야 하고,
    약한 주사위와 candidate의 비교에서 약한 주사위가 이기는 횟수가 9 이상이어야 함.
    """
    win_count = 0
    for c in candidate:
        for s in strong:
            if c > s:
                win_count += 1
    loss_count = 0
    for t in weak:
        for c in candidate:
            if t > c:
                loss_count += 1
    return win_count >= 9 and loss_count >= 9

def is_c_possible(a, b):
    # 먼저 a와 b 중 어느 쪽이 강한 주사위인지 정한다.
    if beats(a, b):
        strong, weak = a, b
    elif beats(b, a):
        strong, weak = b, a
    else:
        # a와 b가 비기는 경우에는 비이행적 구조를 만들기 어렵다고 봄.
        return False
    
    # 극단 조건: 강한 주사위에 10이 3개 이상 있거나, 약한 주사위에 1이 3개 이상 있으면 candidate C는 절대 불가능.
    if strong.count(10) >= 3 or weak.count(1) >= 3:
        return False

    # 정렬하여 비교를 단순화 (순서는 상관없으므로)
    strong = sorted(strong)
    weak = sorted(weak)
    
    # candidate die의 면은 순서와 상관없이 조합으로 볼 수 있으므로, 오름차순 조합(중복 허용)으로 후보를 생성.
    # 경우의 수: (10 + 4 - 1)C4 = 715가지.
    for candidate in combinations_with_replacement(range(1, 11), 4):
        if candidate_possible(strong, weak, candidate):
            return True  # 조건을 만족하는 candidate가 하나라도 있으면 존재함.
    return False

# 입력 처리 (표준 입력 사용)
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    numbers = list(map(int, input().split()))
    a = numbers[:4]
    b = numbers[4:]
    print('yes' if is_c_possible(a, b) else 'no')
