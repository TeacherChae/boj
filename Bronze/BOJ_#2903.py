N = int(input())
point_per_side = 2
for i in range(N):
    point_per_side = (2 * point_per_side) - 1
points = (point_per_side) ** 2
print(points)