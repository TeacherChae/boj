grid = {}
i = 0
max_row = []

for i in range(9):
    a = list(map(int, input().split()))
    grid[i] = a
    max_row.append(max(a))
    i += 1

max_coord = []
for i in range(9):
    if max(grid[i]) == max(max_row):
        j = grid[i].index(max(max_row))
        max_coord.append((i+1,j+1))
print(max(max_row))
print(*max_coord[0])
