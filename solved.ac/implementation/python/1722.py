import sys; input = sys.stdin.readline

n = int(input())
[problem_number, *temp] = list( map(int, input().split()) )

lst = [i for i in range(1, n + 1)]


def find_kth(cnt, permutation):
  global temp


  # print(cnt, permutation)
  # print(n, "?")

  if len(permutation) == n:
    cnt += 1



  if len(permutation) == n and cnt == temp[0]:
    print(*permutation)
    return


  
  for i in range(1, n + 1):
    if visited[i]:
      continue
    visited[i] = True
    find_kth(cnt , permutation + [i])
    visited[i] = False

if problem_number == 1:
  cnt = 0
  visited = [False] * (n + 1)
  print( find_kth(0, []) )
  