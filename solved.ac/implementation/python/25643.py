import sys; input = sys.stdin.readline

n, m = map(int ,input().split())

words = []
for _ in range(n):
  words.append(input().rstrip())

check = True

for i in range(n-1):

  # print(check)
  if words[i] == words[i+1]:
    continue


  for j in range(1, m):
    if words[i][j:] == words[i+1][:m-j]:
      break
    if words[i+1][j:] == words[i][:m-j]:
      break
  else:
    check = False
    break


print(1 if check else 0)
   
