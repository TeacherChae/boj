N = int(input())
paper = [[0]*100 for _ in range(100)]
'''
paper = [
[0, 0, 0, ..., 0],
[0, 0, 0, ..., 0],
[0, 0, 0, ..., 0],
...,
[0, 0, 0, ..., 0]
]
'''
print(paper)

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[j][i] = 1 

answer = 0
for row in paper:
    answer += sum(row)

print(answer)
