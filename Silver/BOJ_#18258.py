import sys
from collections import deque

input_data = sys.stdin.buffer.read().splitlines()
N = int(input_data[0])
q = deque()
results = []

for line in input_data[1:]:
    parts = line.split()
    cmd = parts[0].decode()  # buffer의 경우 바이트형태이므로 디코딩 필요
    if cmd == 'push':
        q.append(int(parts[1]))
    elif cmd == 'pop':
        results.append(str(q.popleft() if q else -1))
    elif cmd == 'size':
        results.append(str(len(q)))
    elif cmd == 'empty':
        results.append("0" if q else "1")
    elif cmd == 'front':
        results.append(str(q[0] if q else -1))
    else:  # 'back'
        results.append(str(q[-1] if q else -1))

sys.stdout.write("\n".join(results))