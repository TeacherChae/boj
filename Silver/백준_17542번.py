R, C = map(int, input().split())
r = input().split()
c = input().split()
x = [int(i) for i in r]
y = [int(i) for i in c]

if max(x) == max(y):
    print('possible')
else:
    print('impossible')