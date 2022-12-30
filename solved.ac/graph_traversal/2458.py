import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]


for _ in range(m):
  v, e = map(int, input().split())
  arr[v-1][e-1] = 1


for path in range(n):
  for i in range(n):
    for j in range(n):


      if arr[i][path] == 1 and arr[path][j] == 1:
        arr[i][j] = 1


answer = 0

for i in range(n):
  check = 0

  for j in range(n):

    check += arr[i][j] + arr[j][i]

  if check == n-1:
    answer += 1

print(answer )