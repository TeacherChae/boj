n,s = map(int, input().split())
refill_cnt = 0
water_left = s
for i in range(n):
    order = input()
    if len(order) >1: # len(espresso) = 1, len(latte) = 2
        ounce = int(order[0]) + 1
    else :
        ounce = int(order[0])
    if water_left < ounce: # 물탱크에 물이 부족하면
        water_left = s - ounce # 물을 가득 채운다
        refill_cnt += 1
    else :
        water_left -= ounce
print(refill_cnt)