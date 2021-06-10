# n = 1  1
# n = 2  3
# n = 3  5
# n = 4  
# n = 5


n = int(input())


d = [0] * 1001

d[1] =1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 *d[i-2]) % 796796