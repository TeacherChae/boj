import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'pop':
        if not deq:
            print(-1)
        else:
            out = deq.popleft()
            print(out)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0) 
    elif cmd[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
    else:
        deq.append(cmd[1])