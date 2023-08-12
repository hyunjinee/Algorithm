n, m = map(int ,input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []
def dfs():
  if len(temp ) == m :
    print(* temp)
    return 
  zoker = 0
  for i in range(n):
    if not visited[i] and zoker != nums[i]:
      visited[i] = True
      temp.append(nums[i])
      zoker = nums[i]
      dfs()
      visited[i] = False
      temp.pop()
dfs()
# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline
# n, m = map(int,input().split())
# l = list(map(int, input().split()))
# l.sort()
# s = []
# d = set()
# visited = [False] * n
# def dfs(depth):
#   if len(s) == m :
#     print(' '.join(map(str, s)))
#     d.add(tuple(s))
#   for i in range(depth, len(l)):
#     if not visited[i]:
#       s.append(l[i])
#       visited[i] = True
#       dfs(depth + 1)
#       s.pop()
#       visited[i] = False
# dfs(0)



# print(list(d))