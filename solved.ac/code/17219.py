import sys
input = sys.stdin.readline
n,m = map(int,input().split())
site = {}
for _ in range(n):
  a, b = input().split()

  site[a] = b


# print(site)


for _ in range(m):
  find = input().rstrip()
  print(site[find])