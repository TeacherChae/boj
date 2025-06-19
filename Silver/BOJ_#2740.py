'''
문제
N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

예제 입력 1 
3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3
예제 출력 1 
-1 -2 6
-3 -6 12
-5 -10 18
'''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
M, K = map(int, input().split())
B = []
for _ in range(M):
    a = list(map(int, input().split()))
    B.append(a)


for i in range(N):
    row = []
    for j in range(M-1):
        a, b = A[i][j], A[i][j+1]
        for k in range(M-1):
            for l in range(K):
                u, x = B[k][l], B[k+1][l]
                element = a*u + b*x
                row.append(element)
    print(*row)

'''
[[1, 2], [3, 4], [5, 6]]
[[-1, -2, 0], [0, 0, 3]]

matrix = []
for i in range(N):
    for j in range(M-1):
        a, b = A[i][j], A[i][j+1]
        row = []
        for k in range(M-1):
            for l in range(K):
                element = a*B[k][l] + b*B[k+1][l]
                row.append(element)
        matrix.append(row)
print(matrix)

[[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1], A[0][0] * B[0][2] + A[0][1] * B[1][2]]]


'''