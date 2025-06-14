# T = int(input())
# for _ in range(T):
#     N = int(input())
#     h = list(map(int, input().split()))


'''
어느 그룹을 뽑든 특정 건초 선호도가 과반을 넘어야 한다.

N = 5일 때
그룹 개체수 = k

가능한 그룹의 수 = 
cnt = 0
for k in range(2, N+1):
    cnt += N - k + 1
cnt = N(N-1) - (N(N+1)/2 - 1) + 1 = N(N-3)/2 + 2

-> 둘다 같아야 성립.

가능한 테스트의 경우가 어떻게 되지?
일단 과반의 정의부터.
-> 특정 건초 수 >= N // 2 + 1

h = [1, 1, 2, 2, 2]
이 경우에도 1이 가능함
idx 0~2까지 그룹 -> 1, 1, 1, 2, 2
전체 그룹 -> 1, 1, 1, 1, 1

h = [1, 2, 1, 2, 2]

흐으음...
N = 2일 때는 예외처리 -> 둘이 같을 때만 가능, 다르면 불가능
N >= 3일 때,  3개로 묶었는데 과반인 수가 존재하면
'''
from collections import deque, Counter

def argmax(n: list):
    best = max(set(n), key=n.count)
    return best if n.count(best) > len(n) / 2 else None

T = int(input())
for _ in range(T):
    N = int(input())
    h = list(map(int, input().split()))
    if N == 2:
        if len(set(h)) == 2:
            print(-1)
        else:
            print(set(h))
    else:
        i = 0
        j = i+3
        # 3개씩 묶기
        set_deq = set()
        deq = deque(h[i:j])
        while j < len(h):
            if argmax(deq):
                # 검사 후 set_deq에 중복없이 저장
                set_deq.add(argmax(deq))
            deq.popleft()
            deq.append(h[j])
            j += 1

        if set_deq:
            sorted_set = sorted(set_deq)
            print(*sorted_set)
        else:
            print(-1)