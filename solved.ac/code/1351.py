from collections import defaultdict

n, p,q  = map(int ,input().split())
a = []

data = defaultdict(int)
data[0] = 1

def dfs(n):
  if data[n] != 0 :
    return data[n]
  
  data[n] = dfs(n//p) + dfs(n//q)
  return data[n]


print(dfs(n))