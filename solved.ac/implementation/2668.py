t = int(input())
adj = [[] for _ in range(t + 1)]
for i in range(t):
  adj[i+1].append(int(input()))

def dfs(v, i ):
  visited[v] = True
  for w in adj[v]:
    if not visited[w]:
      dfs(w, i)
    elif w == i:
      result.append(i)

result = []
for i in range(1, t + 1):
  visited = [False] * ( t + 1)
  dfs(i, i)

l = len(result)
print(l)

for i in range(l):
  print(result[i])