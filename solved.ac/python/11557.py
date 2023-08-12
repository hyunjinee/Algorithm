T = int(input())
school = []
lst =[]
for i in range(T):
    N = int(input())
    for j in range(N):
        S, L = map(str, input().split())
        school.append(S)
        lst.append(int(L))
    max = 0
    for num in lst:
        if max < num:
            max = num
    index = lst.index(max)
    print(school[index])
    