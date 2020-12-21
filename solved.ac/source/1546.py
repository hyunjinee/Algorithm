N = int(input())
scores = list(map(int, input().split()))
newscores =[]
for score in scores:
    score = score/max(scores)*100
    newscores.append(score)



sum = 0
for newscore in newscores:
    sum += newscore

print(sum/N)