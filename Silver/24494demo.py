
# correct, guess 리스트화
correct = []
guess = []
for i in range(3):
    var = str(input())
    for j in range(len(var)):
        correct.append(var[j])
for i in range(3):
    var = str(input())
    for j in range(len(var)):
        guess.append(var[j])

count_green = 0
visited = []
check = 0
for i in range(len(correct)):
    for j in range(len(guess)):
        # 하나씩 비교
        if correct[i] == guess[j]: # 같은 원소를 갖고 있을 때
            if guess[j] not in visited: # 새롭게 탐색하는 원소라면
                if i != j: # 위치가 다를 때
                    visited.append(guess[j]) # visited에 추가
                    count_guess = guess.count(guess[j]) # guess에 등장하는 횟수 세기 (green의 경우도 포함)
                    count_correct = correct.count(guess[j]) # correct에 등장하는 횟수 세기 (green의 경우도 포함)
                    check += min(count_guess, count_correct) # 두 횟수 중 작은 것 반영
                else: # 같은 원소를 갖고 있고 그 위치 또한 같을 때
                    count_green += 1
                    check -= 1

print(count_green)
print(check)

# count_green = len(green)
# new_yellow = list(dict.fromkeys(yellow))
# count_yellow = 0
# for item in new_yellow:
#     a = guess.count(item)
#     b = correct.count(item)
#     count_yellow += min(a,b)
#     for jtem in green:
#         if item == jtem:
#             count_yellow -= 1


correct = []
guess = []
for i in range(3):
    var = input().strip()
    for ch in var:
        correct.append(ch)
for i in range(3):
    var = input().strip()
    for ch in var:
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
for ch in non_green_guess:
    if ch not in visited:
        visited.append(ch)
        yellow += min(non_green_correct.count(ch), non_green_guess.count(ch))

print(count_green)
print(yellow)