N = int(input())
cnt = 0
for i in range(N, 0, -1):
    while i % 5 == 0:
        cnt += 1
        i /= 5
print(cnt)



# N_f = 1
# for i in range(N, 0, -1):
#     N_f *= i
# print(N_f)
# new_f = N_f
# cnt = 0
# while new_f % 10 == 0:
#     new_f /= 10
#     cnt += 1
#     print(new_f)
# print(cnt)