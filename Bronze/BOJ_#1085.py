x, y, w, h = map(int, input().split())
min_x = min(w-x, x)
min_y = min(h-y, y)
print(min(min_x, min_y))