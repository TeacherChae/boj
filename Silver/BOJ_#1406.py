import sys

input_data = sys.stdin.read().splitlines()
left = list(input_data[0].rstrip())
right = []
M = int(input_data[1])

for line in input_data[2:]:
    if line[0] == 'L':
        if left:
            right.append(left.pop())
    elif line[0] == 'D':
        if right:
            left.append(right.pop())
    elif line[0] == 'B':
        if left:
            left.pop()
    else:  # 'P x'
        left.append(line[2])
        
sys.stdout.write(''.join(left + right[::-1]))