#27866번
# S = str(input())
# i = int(input())
# print(S[i-1])

#2743번
# S = str(input())
# print(len(S))

#9086번
# T = int(input())
# for i in range(T):
#     strings = str(input())
#     print(strings[0]+strings[-1])

#11654번
# print(ord(input()))

#11720번
# N = int(input())
# number = list(map(int, input()))
# print(sum(number))

#10809번
# S=str(input())
# list = []
# for i in range(97,123):
#     alphabet = chr(i)
#     number = S.find(alphabet)
#     if number <0:
#         list.append(-1)
#     else :
#         list.append(number)

#2675번
# print(*list)
# T=int(input())
# for i in range(T):
#     R, S = input().split()
#     for j in range(len(S)):
#         print(S[j]*int(R), end='')
#     print()

#1152번
# String = input().split()
# print(len(String))

#2908번
# A,B=map(str, input().split())
# rA = int(''.join(reversed(A)))
# rB = int(''.join(reversed(B)))
# print(max(rA,rB))

#5622번
# # 0. input받기
# words = input()  # 문자열 입력받기
# letters = [element for element in words]  # 각 문자를 리스트로 분리

# # 1. 각 문자가 지시하는 숫자 정의
# alphabet_dict = {
#     2: ['A', 'B', 'C'],
#     3: ['D', 'E', 'F'],
#     4: ['G', 'H', 'I'],
#     5: ['J', 'K', 'L'],
#     6: ['M', 'N', 'O'],
#     7: ['P', 'Q', 'R', 'S'],
#     8: ['T', 'U', 'V'],
#     9: ['W', 'X', 'Y', 'Z']
# }

# nums = []
# for alphabet in letters:
#     for key, value in alphabet_dict.items():
#         if alphabet.upper() in value:  # 대소문자 구분 없이 비교
#             nums.append(key)
#             break  # 매칭되는 숫자를 찾으면 루프 종료

# # 2. 각 숫자까지 도달하는 데 걸리는 시간 정의
# time = []
# for num in nums:
#     time.append(num + 1)  # 숫자에 1을 더한 값이 소요 시간

# # 3. 시간 합계
# print(sum(time))

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)

#11718번
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
