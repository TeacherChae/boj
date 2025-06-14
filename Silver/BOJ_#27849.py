# 하루에 건초 하나 소비
# 총 건초량, 잔여 건초량
# T일 동안 진행되는 소비
# T일 동안의 총 건초 소비량
# 잔여 건초량이 0이 될 때까지는 진행

# N, T = map(int, input().split())
# days = []
# haybales = []
# for i in range(N):
#     day, haybale = map(int, input().split())
#     days.append(day)
#     haybales.append(haybale)
# haybale_consumed = 0
# count_haybale = 0
# for i in range(len(days)):
#     count_day = days[i]
#     count_haybale += haybales[i]
#     if count_day == 5:
#         if count_haybale > 0:
#             haybale_consumed += 1
#     while count_day < T: # 날짜가 다하기 전까지
#         if count_haybale == 0: # 추가 보급이 필요하면
#             break # count_day 갱신
#         else: # 추가 보급이 필요 없으면 필요할 때까지 소비
#             count_haybale -= 1
#             haybale_consumed += 1
#         count_day += 1 # 날짜 경과
# print(haybale_consumed)

N, T = map(int, input().split())
count_days = 0
count_haybales = 0
haybale_consumed = 0
for i in range(N):
    day, haybale = map(int, input().split())
    count_days = day
    count_haybales += haybale
    print(count_days, count_haybales)
    if count_days == 5:
        if count_haybales > 0:
            haybale_consumed += 1
    while count_days < T: # 날짜가 다하기 전까지
        if count_haybales == 0: # 추가 보급이 필요하면
            break # count_day 갱신
        else: # 추가 보급이 필요 없으면 필요할 때까지 소비
            count_haybales -= 1
            haybale_consumed += 1
        count_days += 1 # 날짜 경과
    print(haybale_consumed)
print(haybale_consumed)