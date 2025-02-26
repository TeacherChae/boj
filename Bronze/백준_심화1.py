#3003번
# Full_Pieces = [1, 1, 2, 2, 2, 8]
# Current_Pieces = list(map(int, input().split()))
# Pieces_needed = []
# for i in range(len(Full_Pieces)):
#   amount_needed = Full_Pieces[i] - Current_Pieces[i]
#   Pieces_needed.append(amount_needed)
# print(*Pieces_needed)

#2444번
# N = int(input())
# my_list = []
# for i in range(N, 2*N):
#     my_list.append(i)
# reversed_list = my_list[::-1]
# reversed_lis = reversed_list[1:]
# final_list = my_list+reversed_list
# for i in range(N):
#     star = '*'*(2*i+1)
#     number = i+N
#     print(f'{star:>{number}}')
# for i in range(N-2,-1, -1):
#     star = '*'*(2*i+1)
#     number = i+N
#     print(f'{star:>{number}}')

# n = int(input())
# for i in range(1, n):
#     print(' '*(n-i) + '*'*(2*i-1))
# for i in range(n, 0, -1):
#     print(' '*(n-i) + '*'*(2*i-1))

#10988번
# my_string = list(str(input()))
# if my_string == my_string[::-1]:
#     print(1)
# else:
#     print(0)

#1316번
N=int(input())
unique = []
num = 0
i = 0
j = 0
k = 0
for _ in range(N):
    word = str(input())
    #조건이 맞으면 num+=1
    while i < len(word)-1:
        if word[i+1] != word[i]:
            unique.append(word[i])
            i+=1
        else:
            i+=1
    while j < len(word):
        if unique.count(word[j]) >= 2:
            break
        else:
            j+=1
            k+=1
    if k > 0:
        num += 1
print(num)
            