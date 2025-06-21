'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def n_queen(n):
    visited = [-1] * n
    cnt = 0
    
    def is_ok(row):
        for c in range(row):
            if visited[c] == visited[row] or row - c == abs(visited[row] - visited[c]):
                return False
        return True
    
    def dfs(row):
        if row >= n:
            nonlocal cnt
            cnt += 1
            return
        for i in range(n):
            visited[row] = i
            if is_ok(row):
                dfs(row+1)
                        
    dfs(0)
    return cnt

N = int(input())
print(n_queen(N))

#------------------------------#

def n_queen(n):
    def dfs(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        # 가능한 모든 자리 비트 (1이 빈자리)
        bits = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 가장 오른쪽 1비트만 남김
            bits -= p
            count += dfs(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)
        return count

    return dfs(0, 0, 0, 0)

N = int(input())
print(n_queen(N))