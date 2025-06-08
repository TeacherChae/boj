N = int(input())
l_d = 1
count = 1
while True:
    if N <= l_d:
        break
    l_d += (6*count)
    count += 1
print(count)


        
