correct = []
guess = []
for i in range(3):
    var = input()
    for item in var:
        correct.append(ch)
for i in range(3):
    var = input()
    for item in var:
        guess.append(ch)

# green 처리: 같은 인덱스에서 문자가 일치하면 green
count_green = 0
non_green_correct = []
non_green_guess = []

for i in range(len(correct)):
    if correct[i] == guess[i]:
        count_green += 1
    else:
        non_green_correct.append(correct[i])
        non_green_guess.append(guess[i])

# non-green 위치에서 각 문자별 yellow 개수를 계산
yellow = 0
visited = []
for item in non_green_guess:
    if item not in visited:
        visited.append(item)
        yellow += min(non_green_correct.count(item), non_green_guess.count(item))

print(count_green)
print(yellow)

# guess의 원소가 correct 안에 있는지
# 몇개 있는지 -> guess안 갯수와 correct안 갯수가 서로 크고 작은지(green, yellow 각각)

# # 1) 입력 받기 (3줄 정답, 3줄 추측)
# answer = [input() for _ in range(3)]
# guess  = [input() for _ in range(3)]

# # Green, Yellow 계산에 필요한 변수
# green_count = 0
# freq_answer = [0] * 26  # 정답에서 남아 있는 문자 빈도
# freq_guess  = [0] * 26  # 추측에서 남아 있는 문자 빈도

# # 2) Green 확인 & 빈도 계산
# for i in range(3):
#     for j in range(3):
#         if answer[i][j] == guess[i][j]:
#             # 위치, 문자가 정확히 일치하면 Green
#             green_count += 1
#         else:
#             # 일치하지 않는 문자들만 각 빈도에 반영
#             ans_idx = ord(answer[i][j]) - ord('A')
#             gue_idx = ord(guess[i][j])  - ord('A')
#             freq_answer[ans_idx] += 1
#             freq_guess[gue_idx]  += 1
# print(freq_answer)
# print(freq_guess)
# # 3) Yellow 계산
# # 남은 문자들 중에서 서로 매칭될 수 있는 개수를 센다.
# yellow_count = 0
# for k in range(26):
#     yellow_count += min(freq_answer[k], freq_guess[k])

# # 4) 결과 출력
# print(green_count)
# print(yellow_count)