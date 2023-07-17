a, b = map(int, input().split())
dic = {}
for i in range(a):
    k = input()
    s = ""
    for j in k:
        s += j
        dic[s] = 1
ans = 0
for i in range(b):
    k = input()
    if k in dic:
        ans += 1
print(ans)