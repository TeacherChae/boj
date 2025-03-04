class RoundDigits:
    def __init__(self, n):
        self.num_int = int(n)
        self.num_str = str(self.num_int)
        self.num_P = len(self.num_str)

    def rounding(self):
        if int(self.num_str[0]) >= 5:
            return 10**self.num_P
        else:
            return 0

    def chain_rounding(self):
        current = self.num_int
        for i in range(1, self.num_P+1):
            power = 10 ** i
            # current에서 오른쪽 i번째 자리의 숫자를 구합니다.
            digit = (current // (power // 10)) % 10
            if digit >= 5:
                current += power
            current = (current // power) * power
        return current

    def count_difference(self):
        if self.rounding() == self.chain_rounding():
            return 0
        else:
            return 1



N = int(input())
for i in range(N):
    count = 0
    x = input()
    for j in range(2, int(x)+1):
        J = RoundDigits(j)
        count += J.count_difference()
    print(count)