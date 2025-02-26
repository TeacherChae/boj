#1

number = list(map(int, input().split()))
number.sort()
order = list(input())
new_order = sorted(order)
chart = dict(zip(new_order, [x for x in range(len(order))]))
result = []
for i in range(len(order)):
    result.append(number[chart[order[i]]])
print(*result)

#2
# 입력 처리
number = sorted(map(int, input().split()))  # 입력 숫자 정렬
order = input()                            # 문자 순서 입력

# 문자와 정렬된 숫자 매핑
char_to_num = dict(zip(sorted(order), number))

# 결과 생성 (문자 순서에 따라 숫자 매핑)
result = [char_to_num[char] for char in order]

# 출력
print(*result)
