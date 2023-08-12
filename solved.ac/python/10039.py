scores=[]
for i in range(5):
    a = int(input())
    if(a<40):
        a= 40
    scores.append(a)

sum = 0
for score in scores:
    sum += score
print(int(sum/5))
