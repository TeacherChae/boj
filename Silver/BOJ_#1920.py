N = int(input())
A = set(map(int, input().split()))

M = int(input())
M_int = map(int, input().split())

for i in M_int:
    print(1 if i in A else 0)