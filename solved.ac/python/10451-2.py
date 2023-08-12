T = int (input())

def bfs(V):
  queue = [V]
  visited[V] = 1
  while queue:
    V = queue[0]
    queue.pop(0)
    next = arr[V]
    if visited[next] == 0:
      visited[next] = 1
      queue.append(next)
    
  return 1
  

for i in range(T):
  answer = 0 
  N = int (input())
  arr = [0] + list(map(int, input().split()))

  visited = [0] * (N+1)

  for i in range(1, N+1):
    if visited[i] == 0:
      answer += bfs(i)
  print(answer)