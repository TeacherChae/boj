import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    h = list(map(int, input().split()))

    # 1) 위치 저장 (1-indexed)
    pos = {}
    for i, x in enumerate(h, start=1):
        if x in pos:
            pos[x].append(i)
        else:
            pos[x] = [i]


    ans = []
    half = N // 2           # 과반: k > half
    for x, plist in pos.items():
        k = len(plist)
        if k > half:
            ans.append(x)
        elif k < 2:
            continue
        else:
            # 인접 등장 두 소의 차이가 2 이하인 쌍 찾기
            for i in range(k-1):
                if plist[i+1] - plist[i] <= 2:
                    ans.append(x)
                    break

    if ans:
        ans.sort()
        print(*ans)
    else:
        print(-1)