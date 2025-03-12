result = ['Invalid','Equilateral','Isosceles','Scalene']
while True:
    c = [*map(int, input().split())]
    if sum(c) == 0:
        break
    index = sum(c) - max(c) > max(c)
    print(result[index * len({*c})])