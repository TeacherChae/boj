#11021번
'''
import sys
T = int(input())
for i in range(1,T+1):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i}: {a+b}")
'''

#2438번
'''
N = int(input())
for i in range(1, N+1):
    ans = '*'*i
    print(ans)
'''

#2439번
'''
N=int(input())
for i in range(1,N+1):
    print(f"{'*'*i:>{N}}")
'''

#10952번
'''
while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0 or a >= 10 or b >= 10:
        break
    c = a + b
    print(c)
'''

#10951번
'''
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
'''