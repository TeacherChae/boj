#상근 = ABCABCABC...
#창영 = BABCBABCBABC...
#현진 = CCAABBCCAABB...

Answer_Length = int(input())
Answer = str(input())
Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']
Adrian_correct, Bruno_correct, Goran_correct = 0, 0, 0
for i in range(Answer_Length):
    if Answer[i] == Adrian[i%len(Adrian)]:
        Adrian_correct += 1
    if Answer[i] == Bruno[i%len(Bruno)]:
        Bruno_correct += 1
    if Answer[i] == Goran[i%len(Goran)]:
        Goran_correct += 1

print(max(Adrian_correct, Bruno_correct, Goran_correct))
if max(Adrian_correct, Bruno_correct, Goran_correct) == Adrian_correct:
    print('Adrian')
if max(Adrian_correct, Bruno_correct, Goran_correct) == Bruno_correct:
    print('Bruno')
if max(Adrian_correct, Bruno_correct, Goran_correct) == Goran_correct:
    print('Goran')