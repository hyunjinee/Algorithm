N= int(input())
lst =[]
for i in range(N):
    old, name = map(str , input().split())
    old = int(old)
    lst.append((old, name))
lst.sort(key = lambda member: (member[0]))

for i in range(N):
    print(lst[i][0],lst[i][1])
