N = int(input())
a = list(map(int, input().split()))
a.sort()
total_p = 0
for i, item in enumerate(a):
    total_p += (N-i) * item
print(total_p)