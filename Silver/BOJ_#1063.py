def move(x, y, command):
    '''
    command의 종류에 따라서 object의 위치를 갱신해준다.
    '''
    if command == 'R':
        x += 1
    if command == 'L':
        x -= 1
    if command == 'T':
        y += 1
    if command == 'B':
        y -= 1
    if command == 'RT':
        x += 1
        y += 1
    if command == 'LT':
        x -= 1
        y += 1
    if command == 'RB':
        x += 1
        y -= 1
    if command == 'LB':
        x -= 1
        y -= 1
    return x, y

king, stone, N = map(str, input().split())
N = int(N)
x, y = ord(king[0]), ord(king[1])
w, z = ord(stone[0]), ord(stone[1])
for i in range(N):
    command = input()
    new_x, new_y = move(x, y, command)
    new_w, new_z = w, z
    if new_x == w and new_y == z:
        new_w, new_z = move(w, z, command)
    if (65 <= new_x <= 72 and 65 <= new_w <= 72 and
        49 <= new_y <= 56 and 49 <= new_z <= 56):
        x, y, w, z = new_x, new_y, new_w, new_z
    else:
        continue
king = chr(x) + chr(y)
stone = chr(w) + chr(z)
print(king)
print(stone)