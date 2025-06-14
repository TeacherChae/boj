N = int(input())
serial = 665
idx = 0
while True:
    serial += 1
    if '666' in str(serial):
        idx += 1
    if idx == N:
        break
print(serial)