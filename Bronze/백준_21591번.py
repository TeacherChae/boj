w_e, h_e, w_s, h_s = map(int, input().split())
if (w_e - w_s)>=2 and (h_e - h_s)>=2:
    print(1)
else:
    print(0)