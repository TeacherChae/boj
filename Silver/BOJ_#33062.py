# ex) 23 -> P : 2, 234 -> P : 3
# x의 범위는 range(2, N+1)
# x가 10^1 자리수면 P = 2
# 즉, if x>=10**(i) and x<10**(i+1): P = i
# def count_digits(n):
#     if n < 10:
#         return 1
#     else:
#         return 1 + count_digits(n // 10)

# def rounding(n):
#     if (n*10 // 10**count_digits(n)) >= 5:
#         return 10**count_digits(n)
#     else:
#         return 10**(count_digits(n)-1)

# #

# def chain_rounding(n):
#     for i in range(1, count_digits(n)):
#         a = n % (10**i)
    


#input을 str으로 받으면

def rounding(n):
    if int(n[0]) >= 5:
        return 10**len(n)
    else:
        return 10**(len(n)-1)

def chain_rounding(n):
    results = []
    for i in range(1, len(n)+1):
        a = int(n) % (10 ** i)
        if str(a)[0] >= 5:
            result = int(n) - a + (10**len(a))
            results.append(result)
        else:
            result = int(n) - a
            results.append(result)
    return results

x = str(input())
print(rounding(x))
print(chain_rounding(x))
