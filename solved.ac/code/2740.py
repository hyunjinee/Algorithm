import sys
input = sys.stdin.readline

n, m = map(int,input().rsplit())
a = []
for _ in range(n):
    row = list(map(int,input().rsplit()))
    a.append(row)

m, k = map(int,input().rsplit())
b = []
for _ in range(m):
    row = list(map(int,input().rsplit()))
    b.append(row)
    
result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            result[i][j] += a[i][t] * b[t][j]

for row in result:
    for num in row:
        print(num, end=" ")
    print()