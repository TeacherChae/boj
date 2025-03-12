N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

len_X = max(X) - min(X)
len_Y = max(Y) - min(Y)
print(len_X * len_Y)