import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[] for i in range(n)]
visited = [False] * n

def dfs(idx, number) :
  if number == 4:
    print(1)
    exit()
  for i in arr[idx]:
    if not visited[i]:
      visited[i] = True
      dfs(i, number+1)
      visited[i] = False


for _ in range(m):
  a, b =map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)


for i in range(n):
  visited[i] = True
  dfs(i,0)
  visited[i] = False
print(0)