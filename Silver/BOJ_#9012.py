import sys
from collections import deque

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
results = []

for line in input_data[1:]:
    deq = deque()
    for char in line:
        if char == '(': # 여는 괄호면 추가
            deq.append(char)
        else: # 닫는 괄호인데
            if deq: # 여는 괄호가 남아있으면
                deq.pop() # pop
            else: # 여는 괄호가 남아있지 않으면 == 닫는 괄호만 있으면
                deq.append(char) # 일단 추가하고
                break # 그 즉시 for문 종료
    # 한 라인을 다 돌았는데 deq가 남아있으면(여는 쪽이든 닫는 쪽이든)
    if deq:
        results.append('NO')
    else:
        results.append('YES')
        
sys.stdout.write("\n".join(results))