N, S = map(int, input().split())

pos_info = [None] * (N + 1)
for i in range(1, N + 1):
    q, v = map(int, input().split())
    pos_info[i] = (q, v)

# 초기화
pos = S
power = 1
direction = 1  

broken_count = 0
broken = [False] * (N + 1)

q, v = pos_info[pos]
if q == 0:
    power += v
    direction *= -1
else:
    if power >= v and not broken[pos]:
        broken[pos] = True
        broken_count += 1

visited = set()
visited.add((pos, direction, power))

while True:
    next_pos = pos + direction * power
    if next_pos < 1 or next_pos > N:
        break
    
    pos = next_pos
    q, v = pos_info[pos]
    if q == 0:
        power += v
        direction *= -1
    else:
        if power >= v and not broken[pos]:
            broken[pos] = True
            broken_count += 1

    state = (pos, direction, power)
    if state in visited: # pos, direction, power가 모두 동일한 경우 무한 루프에 빠진 것으로 간주.
        break
    visited.add(state)

print(broken_count)
