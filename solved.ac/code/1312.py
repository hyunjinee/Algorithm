from sys import stdin

a,b,n = map(int,stdin.readline().split())

a %= b

for i in range(n-1):
    a = (a * 10) % b

print((a*10)//b)

# a,b,n = map(int,input().split())
# for i in range(n):
# 	a=(a%b)*10
# print(a//b)  

# # a, b, n = map(int, input().split())
# # c = str( a / b )
# # if a % b == 0 :
# #   print(0)
# # else:
# #   d = c.split(".")[1]
# #   print(d)
# #   print(d[n-1])


# # a,b,n=map(int,input().split())
# # print(a*(10**n)//b%10)