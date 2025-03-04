N, B = map(int, input().split())
lst = []
while True:
    num = N % B
    N //= B
    if num < 10:
        value = str(num)
    else:
        value = chr(num + 55)
    lst.append(value)
    if N == 0:
        break

print(''.join(reversed(lst)))
