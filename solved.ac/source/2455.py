count = 0
lst = []
for i in range(4):
    a,b = map(int, input().split())
    count = count -a +b
    lst.append(count)


print(max(lst))