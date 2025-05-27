N, Q = map(int, input().split())

a = []
for i in range(N):
    b = []
    a.append(b)
    for j in range(N):
        c = []
        b.append(c)
        for k in range(N):
            c.append(0)


for _ in range(Q):
    x, y, z = map(int, input().split())
    a[z][y][x] = 1

    cnt = 0
    for z in range(N):
        for y in range(N):
            if a[z][y][0] == 1:
                for x in range(N):
                    if a[z][y][0] != a[z][y][x]:
                        break
                else:
                    cnt += 1
    
    for z in range(N):
        for x in range(N):
            if a[z][0][x] == 1:
                for y in range(N):
                    if a[z][0][x] != a[z][y][x]:
                        break
                else:
                    cnt += 1

    for y in range(N):
        for x in range(N):
            if a[0][y][x] == 1:
                for z in range(N):
                    if a[0][y][x] != a[z][y][x]:
                        break
                else:
                    cnt += 1


    print(cnt)

'''
l[0][0][0] == l[0][0][1] == l[0][0][2] == ... == l[0][0][N-1]을 어떻게 판별하는가.
1. for문으로 직전 값과 계속 비교

cnt = 0

x축

for z in range(N):
    for y in range(N):
        for x in range(N):
            if l[z][y][0] != l[z][y][x]:
                break
        else:
            cnt += 1

y축

for z in range(N):
    for x in range(N):
        for y in range(N):
            if l[z][0][x] != l[z][y][x]:
                break
        else:
            cnt += 1

z축

for y in range(N):
    for x in range(N):
        for z in range(N):
            if l[0][y][x] != l[z][y][x]:
                break
        else:
            cnt += 1

    '''