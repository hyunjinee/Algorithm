T = int(input())

for i in range(T):
    N = list(map(int, input().split(' ')))
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for j in N[1:]:
        if j> avg:
            cnt +=1
    print(str("%.3f" %round((cnt/N[0])*100,3))+"%")


