# 1.
# N = int(input())
# S = list(map(int, input().split()))

# def remove_duplicates(lst):
#     searched = []
#     result = []
#     for item in lst:
#         if item not in searched:
#             result.append(item)
#         searched.append(item)
#     return result

# uniques = remove_duplicates(S)
# if len(uniques) <= 2: # 고유값(과일 종류)이 2 이하일 때는 과일 갯수
#     print(len(S))
# else: # 고유값이 3 이상일 때는 2 이하가 될 때까지 리스트를 줄임
#     slicings = []
#     for i in range(N):
#         # a+b가 0, 1, 2, 3, ..., N-1일 때.
#         for j in range(i+1):
#             # (a, b)가 (0, i)일때, (1, i-1)일 때, (2, i-2)일 때, ..., (i, 0)일 때. 
#             a, b =j, i-j # a+b = i
#             slicing = S[a:N-b] # 왼쪽으로 a만큼, 오른쪽으로 b만큼 제거
#             uniques_slicing = remove_duplicates(slicing) # 고유값 추출
#             if len(uniques_slicing) <= 2: 
#                 slicings.append(len(slicing)) # 고유값 2이하인 경우만 append
#     print(max(slicings)) # slicings의 최댓값 출력


# 2.
def longest_subarray_with_at_most_two_uniques(arr):
    left = 0 # 윈도우의 왼쪽 인덱스
    counts = {} # 원소의 등장 횟수
    max_length = 0 #?

    for right, value in enumerate(arr): # 인덱스와 값 동시 호출
        counts[value] = counts.get(value, 0) + 1 # value가 없으면 0에서 1을 더한 후 key : value 쌍을 생성하고, 있으면 있는대로 1을 더함
        #그냥 +=counts[value] + 1은 안되나? 안됨. 없는 key를 찾으려하면 key error가 생기기 때문.

        # 고유 원소가 2개를 초과하면 왼쪽부터 줄여나갑니다.
        while len(counts) > 2: # 고유 원소가 2개를 초과하면
            counts[arr[left]] -= 1 # 가장 왼쪽의 value에서 하나씩 차감. 언제까지?
            if counts[arr[left]] == 0: # value가 없어질 때까지
                del counts[arr[left]] # 없어지면 원소 삭제
            left += 1 # 그리고 한칸 오른쪽으로 윈도우를 옮김

        max_length = max(max_length, right - left + 1) # 매 iterration마다 이전과 현재의 max_length를 비교.

    return max_length

N = int(input())
S = list(map(int, input().split()))

# 전체 리스트의 고유 원소가 2개 이하이면 전체 길이가 정답입니다.
if len(set(S)) <= 2:
    print(N)
else:
    print(longest_subarray_with_at_most_two_uniques(S))
