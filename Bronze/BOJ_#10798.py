# 1.
word = []
length = []
vertical = []
for i in range(5):
    w = input()
    word.append(w)
    length.append(len(w))
for j in range(max(length)):
    for k in word:
        try:
            vertical.append(k[j])
        except IndexError:
            continue    
print(*vertical, sep = '')

# 2.
words = [input() for _ in range(5)]
max_len = max(len(word) for word in words)
result = []
for i in range(max_len):
    for word in words:
        if i < len(word):
            result.append(word[i])
print(*result, sep='')
