#연속하는 단어라는 게 무슨 의미인지 먼저 정의해야함.
#인접한 중복을 제거하고 하나의 리스트에 담기
#그래도 중복이 있으면 그룹 단어 x
N = int(input())
group_word = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        elif word[j] in word[j+1:] :
            group_word -= 1
            break
print(group_word)
