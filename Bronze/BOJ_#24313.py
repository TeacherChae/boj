a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())
if c < a_1:
    print(0)
elif c == a_1 and a_0 <= 0:
    print(1)
elif c == a_1 and a_0 > 0:
    print(0)
elif n_0 >= (a_0 / (c - a_1)):
    print(1)
else:
    print(0)