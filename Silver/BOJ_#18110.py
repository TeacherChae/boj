import math

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    #1. 전부 받는다.
    ops = []
    for i in range(n):
        ops.append(int(input()))
    #2. 오름차순으로 재정렬한다.
    ops.sort()
    #3. 절사 진행.
    border = roundUp(n * 0.15)
    #4. 평균 구하기.
    print(roundUp(sum(ops[border:n-border])/len(ops[border:n-border])))