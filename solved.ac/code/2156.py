import sys
input= sys.stdin.readline

n = int(input())

a = [0 for _ in range(n+1)]


for i in range(1, n+1) :
    a[i] = int(input())


d = [0 for _ in range(n+1)]

if n == 1:
    print(d[1])

    sys.exit()

d[2] = a[1] + a[2]


for i in range(3, n+1) :
    d[i] = max(d[i-1], d[i-2] + a[i] , d[i-3] + a[i] + a[i-1])

print(d[n])
 