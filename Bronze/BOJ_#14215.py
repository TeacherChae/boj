s = [*map(int, input().split())]
max_e = min(sum(s) - max(s) - 1, max(s))
print(sum(s) - max(s) + max_e)