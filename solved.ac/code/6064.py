def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))

# import sys
# input =sys.stdin.readline

# for _ in range(int(input())):
#   m,n,x,y = map(int,input().split())
#   cnt = 1
#   a , b= 1, 1
#   flag = False
#   while True:
#     if a == m and b == n :
#       break
#     if a == x and b == y :
#       flag = True
#       break
#     if a < m and b < n:
#       a += 1
#       b += 1
#       cnt += 1
#     elif a >= m and  b < n:
#       a = 1
#       b += 1
#       cnt +=1
#     elif b >= n and a < m: 
#       b = 1
#       a += 1
#       cnt +=1
#   if Flag:
#     print(cnt)
#   else: 
#     print(-1)