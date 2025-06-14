H, *rest = input().split()
H = int(H)
path = rest[0] if rest else ''

cur = 1
for c in path:
    cur = cur*2 if c == 'L' else cur*2 + 1

print(2**(H+1) - cur)
