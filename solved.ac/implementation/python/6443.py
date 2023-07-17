import sys
input = sys.stdin.readline

def back_tracking(cnt):
  if cnt == len(word):
    print("".join(answer))

  for k in visited:
    if visited[k]:
      visited[k] -= 1
      answer.append(k)
      back_tracking(cnt + 1)
      visited[k] += 1
      answer.pop()


n = int(input())
for _ in range(n):
  word = sorted(list(map(str, input().rstrip())))
  visited = {}
  answer = []
  for i in word:
    if i in visited:
      visited[i] += 1
    else:
      visited[i] =  1
  back_tracking(0)
