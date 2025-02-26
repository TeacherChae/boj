#1
a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

# 맨해튼 거리 계산
diff = abs(a - c) + abs(b - d)

# 짝수/홀수 확인 함수
def even_number(x):
    return x % 2 == 0

def odd_number(x):
    return x % 2 == 1

# 짝수/홀수에 따라 조건 검사
if even_number(diff) and t>=diff and even_number(t):
    print('Y')
elif odd_number(diff) and t>=diff and odd_number(t):
    print('Y')
else:
    print('N')

#2
a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

# 맨해튼 거리 계산
diff = abs(a - c) + abs(b - d)

# 짝수/홀수 및 조건 검사
if t >= diff and (diff % 2 == t % 2):
    print('Y')
else:
    print('N')