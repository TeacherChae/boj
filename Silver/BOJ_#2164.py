from collections import deque 

N = int(input())
cards = deque(range(1, N+1))
cnt = 0
while len(cards) > 1:
    if len(cards) == 1:
        break
    if cnt % 2 == 0:
        cards.popleft()
    else:
        ltr = cards.popleft()
        cards.append(ltr)
    cnt += 1
print(*cards)