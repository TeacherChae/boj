word = input()

# len(p_word) == 1, 2, 3, ..., n 각각의 경우에 따라
# 부분 문자열 p_word를 전부 구한다
# 이중 for문? 해보지 뭐
p_word = set()
for length in range(1, len(word)+1):
    start = 0 # 시작 인덱스
    end = length # 끝 인덱스
    while end < len(word)+1: # 끝 인덱스가 전체 길이보다 작을 때
        p_word.add(word[start:end])
        start += 1
        end = start+length
print(len(p_word))

# for문으로 set()에 담는다.
# len(set())