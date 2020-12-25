N = int(input())

#N 이 3x+5y 꼴 로 만들 수 있는지 검사
a = []
for i in range(0,1666):
    for j in range(0,1001):
        if 3*i + 5*j == N:
            a.append(i+j)


if len(a) == 0:
    print(-1)
else:
    print(min(a))

  
