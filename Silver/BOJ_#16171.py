S = input()
K = input()
str_S = []
for item in S:
    if item.isalpha():
        str_S.append(item)
str_S = ''.join(str_S)
if K in str_S:
    print(1)
else:
    print(0)