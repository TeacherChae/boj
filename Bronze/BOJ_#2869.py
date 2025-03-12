A, B, V = map(int, input().split())
C = (V - A) / (A - B)
C = int(C) + (C > int(C))
print(C+1)