N, B = input().split()
B = int(B)
digit = 0

for char in N:
    if char.isdigit():
        value = int(char)
    else:
        value = ord(char) - 55
    digit = digit * B + value

print(digit)