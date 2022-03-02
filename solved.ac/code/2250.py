import sys
input = sys.stdin.readline
n = int(input())
graph= [[] for _ in range(n+1)]
isRoot = [0] * (n + 1)
distance = [[] for _ in range(n+1)]
root = 0
for _ in range(n):
  parent, left, right = map(int, input().split())
  graph[parent].append(left)
  graph[parent].append(right)
  isRoot[parent] += 1
  if left != -1:
    isRoot[left] += 1
  if right != -1:
    isRoot[right] += 1
for i in range(1, n+1):
  if isRoot[i] == 1:
    root = i

    
num = 1
def inorder(start, deep):
  global num
  if graph[start][0] != -1:
    inorder(graph[start][0], deep + 1)
  distance[deep].append(num)
  num += 1
  if graph[start][1] != -1:
    inorder(graph[start][1],deep+1)

inorder(root, 1)
level =1 
ans = max(distance[1]) - min(distance[1] ) + 1
for i in range(2, n+1):
  if distance[i]:
    small = min(distance[i])
    large = max(distance[i])
    if ans < large - small + 1:
      ans = large - small + 1
      level = i
print(level, ans)