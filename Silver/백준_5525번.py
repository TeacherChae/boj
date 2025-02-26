


'''
# 초기 윈도우의 합 계산 (문자열을 정수형으로 변환)
current_sum = sum(int(s[i]) for i in range(N))
if some_condition(current_sum):
    # 조건 만족 시 작업

# 슬라이딩 윈도우 적용
for i in range(1, M - N + 1):
    current_sum = current_sum - int(s[i-1]) + int(s[i+N-1])
    if some_condition(current_sum):
        # 조건 만족 시 작업
'''
def Pn(N):
    ioi = ''
    for item in range(2*N+1):
        if item % 2 == 0:
            ioi += 'I'
        else:
            ioi += 'O'
    return ioi

N = int(input())
M = int(input())
S = str(input())
check_Pn = S[:2*N+1]
count = 0

for i in range(1, M-2*N):
    if check_Pn == Pn(N):
        count += 1
    check_Pn = check_Pn[1:] + S[2*N+i]
if check_Pn == Pn(N):
    count += 1
print(count)

###

def Pn(N):
    return ''.join('I' if i % 2 == 0 else 'O' for i in range(2*N+1))

def kmp_search(text, pattern):
    m = len(pattern)
    # lps 배열 (Longest Prefix Suffix) 계산
    lps = [0] * m
    j = 0  # pattern의 인덱스
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    count = 0
    j = 0  # text 내에서의 pattern 인덱스
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                count += 1
                j = lps[j-1]
    return count

N = int(input())
M = int(input())
S = input()
pattern = Pn(N)
print(kmp_search(S, pattern))
