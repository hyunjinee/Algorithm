N, C = map(int, input().split())
c =[0] * (C+1)
for _ in range(N):
    num = int(input())
    if num == 1:
        print(C)
        quit()
    for k in range(num,C+1,num):
        c[k] = 1
print(sum(c))