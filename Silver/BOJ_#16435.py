N, L = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for i in H:
    if i <= L:
        L += 1
print(L)