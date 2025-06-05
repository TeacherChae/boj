def collatz_conjecture(n):
    l = [n]
    while n != 1:    
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        l.append(n)
    return l

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    A = collatz_conjecture(a)
    steps_B = {val: idx for idx, val in enumerate(collatz_conjecture(b))}

    for i, val in enumerate(A):
        if val in steps_B:
            j = steps_B[val]
            print(f'{a} needs {i} steps, {b} needs {j} steps, they meet at {val}')
            break
            

'''
if (n-1) % 3 != 0:
    n *= 2
else:
    n = (n-1) // 3

[[1], [2], [4], [8], [16], [5, 32], [10, 64], [3, 20, 21, 128], ...]

if n % 2 == 0:
    n //= 2
else:
    n = 3*n + 1

'''
