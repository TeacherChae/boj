N = list(range(1, 11))
while True:
    Q = int(input())
    if Q == 0:
        break
    A = str(input())
    if A == 'too high':
        N = [i for i in N if i < Q]
    if A == 'too low':
        N = [i for i in N if i > Q]
    if A == 'right on':
        if Q in N:
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        N = list(range(1, 11))