table, coord = dict(), -1
MOVE = {'L':-1,'R':1,'B':9,'T':-9,'LT':-10,'RT':-8,'LB':8,'RB':10}
for row in '87654321':
	coord += 1
	for col in 'ABCDEFGH':
		coord += 1
		table[col+row] = coord
		table[coord] = col+row
	
king, stone, N = input().split()
king, stone = table[king], table[stone]
for _ in range(int(N)):
	move = MOVE[input()]
	nextK = king + move; nextS = stone + move
	if nextK not in table: continue
	if nextK == stone:
		if nextS not in table: continue
		stone = nextS
	king = nextK
print(table[king], table[stone])