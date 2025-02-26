#1

N = int(input())
number_recited = []
for i in range(N):
    number = int(input())
    number_recited.append(number)
number_origin = list(range(1, number_recited[-1]+1))
length = len(number_origin)
for item in number_origin:
    if item in number_recited:
        length -= 1
    else:
        print(item)
if length == 0:
    print('good job')

# difference = [item for item in number_origin if item not in number_recited]
# print(difference)

#2
N = int(input())
number_recited = {int(input()) for _ in range(N)}  # Set for faster lookup
number_origin = range(1, max(number_recited) + 1)  # Use range directly

missing_numbers = [item for item in number_origin if item not in number_recited]

if missing_numbers:
    print("\n".join(map(str, missing_numbers)))
    #print(*missing_numbers, sep="\n")도 가능
else:
    print('good job')
