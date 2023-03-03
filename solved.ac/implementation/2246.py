condos = []
for i in range(int(input())):
    l, p = map(int, input().split())
    condos.append([l, p])
condos.sort()
cost = 10001
result = 0
for i in condos:
    temp = i[1]
    if temp < cost:
        cost = temp
        result += 1
print(result)