import sys
input = sys.stdin.readline


n, k = map(int, input().split())

a = list(map(int,input().split(",")))


for i in range(k):
  b = []
  for j in range(len(a)- 1):
    b.append(a[j+1] - a[j])
  a = b
ans = ""
for e in a:
  ans += str(e) + ","

print(ans[:-1])
