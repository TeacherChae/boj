score = [int(input()) for _ in range(8)]
top_score = sorted(score)[3:]
order = [score.index(item) + 1 for item in top_score]
order.sort()
print(sum(top_score))
print(*order)