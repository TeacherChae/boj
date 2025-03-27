from collections import deque
    
N, K = map(int, input().split())

deq = deque(range(1, N+1))
josephus = []
while deq:
    deq.rotate(-(K-1))
    josephus.append(deq.popleft())
print('<' + ', '.join(map(str, josephus)) + '>')