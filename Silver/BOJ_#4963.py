while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    matrix = []
    for i in range(h):
        line = list(input().split())
        matrix.append(line)