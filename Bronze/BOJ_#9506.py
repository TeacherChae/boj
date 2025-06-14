while True:
    n = int(input())
    if n == -1:
        break
    factor = [i for i in range(1, n) if n % i == 0]
    index = len(factor)
    factor_sum = sum(factor)
    if n == factor_sum:
        print(f"{n} =", " + ".join(map(str, factor)))
    else:
        print(f'{n} is NOT perfect.')