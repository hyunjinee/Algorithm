import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
ori = p
g = [0, 1, 2] * (n // 3)
k = [0] * n
cnt = 0


while p != g:
    for i in range(n):
        k[s[i]] = p[i]
    p=k
    k = [0] * n
    cnt+=1
    if ori == p:
        cnt =- 1
        break
        
print(cnt)