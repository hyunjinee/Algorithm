n = int(input())
matrosica = list(map(int, input().split()))
matrosica.sort(reverse=True)
visited = [False] * n
cnt = 0 

def make_matrosica():
  temp = -1
  for i in range(len(matrosica)):
    if not visited[i] and temp != matrosica[i]:
      visited[i] = True
      temp = matrosica[i]

while True:
  cnt += 1
  make_matrosica()

  if sum(visited) == len(visited):
    break

print(cnt)