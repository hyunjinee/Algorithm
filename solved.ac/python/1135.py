n = int(input())
t = list(map(int,input().split()))
tree = [[] for _ in range(n)]

for idx in range(1, n):
  tree[t[idx]].append(idx)

time = [False] * n

def dp(v):
  child_t = []
  for nei in tree[v]:
    dp(nei)
    child_t.append(time[nei])
  if not tree[v]:
    child_t.append(0)

  child_t.sort(reverse=True)
  need_time = [child_t[i] + i + 1 for i in range(len(child_t))]
  time[v] = max(need_time)

dp(0)
print(time[0] - 1)