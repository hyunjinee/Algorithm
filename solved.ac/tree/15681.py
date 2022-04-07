import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n,r,q=map(int,input().split())
tree = [[] for _ in range(n+1)]
cnt = [0] * (n+1)

def NodeCount(x):
  cnt[x] = 1
  for i in tree[x]:
    if not cnt[i]:
      NodeCount(i)
      cnt[x] += cnt[i]

for _ in range(n-1):
  u, v = map(int,input().split())
  tree[u].append(v)
  tree[v].append(u)
NodeCount(r)

for i in range(q):
  temp = int(input())
  print(cnt[temp])


# for __ in range(q):
#   temp = int(input())
#   if n == temp: 
#     print(n)
#     continue

#   q = deque()
#   q.append(temp)
#   ans = 0
#   while q:
#     ans += 1

#     node =  q.popleft()
#     for child in tree[node]:
#       q.append(child)

#   print(ans)

