import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x):
  visited[x] = True
  number = numbers[x]
  if not visited[number] :
    dfs(number)

for _ in range(int(input())):
  N = int(input())
  numbers = [0] + list(map(int, input().split()))
  visited = [True] + [False] * N
  result = 0 
  for i in range(1, N+1):
    if not visited[i]:
      dfs( i)
      result += 1
    
  print(result)