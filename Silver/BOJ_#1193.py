# N = int(input())
# intrv_sum = 2 # 각 분수가 위치한 구간의 구간합
# max = 1 # 각 분수가 위치한 구간의 최상단 값
# fraction = []
# while True:
#     for i in range(1, intrv_sum):
#         j = intrv_sum - i
#         if intrv_sum % 2 == 1:
#             pair = (i, j)
#         pair = (j, i)
#         fraction.append(pair)
#     if N > max:
#         max += intrv_sum
#         intrv_sum += 1
#     else:
#         break
# print(*fraction[N-1], sep = '/')

N = int(input().strip())

# 먼저 N이 몇 번째 대각선(diagonal)에 속하는지 찾는다.
# 대각선 번호를 line이라 할 때,
# 1번째 대각선에 들어있는 원소 수는 1,
# 2번째 대각선에 들어있는 원소 수는 2,
# 3번째 대각선에 들어있는 원소 수는 3, ...
# 즉, line 번째 대각선까지 누적 합은 1+2+...+line = line*(line+1)//2
# 이 값이 N 이상이 되는 최초의 line을 찾는다.

line = 1       # 현재 대각선 번호
acc = 1        # 누적 합 (1+2+...+line)
while N > acc:
    line += 1
    acc += line

# N은 'acc'가 넘어서는 순간의 대각선에 위치하게 된다.
# offset은 그 대각선에서 몇 번째 원소인지를 나타낸다.
offset = N - (acc - line)

# line이 홀수인지 짝수인지에 따라 분수 표현(분자/분모) 순서가 달라진다.
if line % 2 == 0:
    # line이 짝수면, (offset / (line-offset+1))
    print(f"{offset}/{line - offset + 1}")
else:
    # line이 홀수면, ((line-offset+1) / offset)
    print(f"{line - offset + 1}/{offset}")
