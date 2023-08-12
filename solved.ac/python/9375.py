from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1
    print(num - 1)