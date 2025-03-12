x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
X = [x1, x2, x3]
Y = [y1, y2, y3]
for item in X:
    if X.count(item) == 1:
        x4 = item
for item in Y:
    if Y.count(item) == 1:
        y4 = item
print(x4, y4)