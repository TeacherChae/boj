N = int(input())
cmd = input().split()
# 리스트 길이가 홀수인 경우, 중간 인덱스를 반환하고 리스트를 쪼갠다. 쪼갠 리스트에 같은 과정을 반복한다.
# 리스트의 길이가 짝수인 경우 멈춘다.

answer = [[] for _ in range(N)]

def bisect(lst, depth):
    mid = len(lst) // 2
    answer[depth].append(lst[mid])
    if len(lst) == 1:
        return
    
    bisect(lst[:mid], depth + 1)
    bisect(lst[mid + 1:], depth + 1)

a = bisect(cmd, 0)
for i in answer:
    print(*i)
