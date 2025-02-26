#10807번
'''
n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))
출처: https://develop247.tistory.com/142 [ImJay:티스토리]
'''
'''
N = int(input()) 
N_list = input()
v = int(input())

if len(N_list.split()) == N :
    number_list = list(map(int, N_list.split()))

print(number_list.count(v))
'''

#10871번
'''
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i<X:
        print(i, end=' ')
'''

#10818번
'''
N = int(input())
N_list = list(map(int, input().split()))
print(min(N_list), max(N_list))
'''

#2562번
# numbers = [int(input()) for _ in range(9)]

# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)

#3052번
# unique = []
# for i in range(10):
#     N = int(input())
#     A = N%42
#     unique.append(A)
# print(len(set(unique)))

#10811번
# N,M = map(int,input().split())
# Box = list(range(1,N+1))
# for _ in range(M):
#     i,j = map(int,input().split())
#     Box[i-1:j]=reversed(Box[i-1:j])
# print(*Box)

#1546번
# N = int(input())
# score = list(map(int, input().split()))
# M = max(score)
# new_score = [num/M*100 for num in score]
# new_average = sum(new_score)/N
# print(new_average)