import sys
input = sys.stdin.readline


while True:
  try:
    n, k = map(int ,input().split())
  except: 
    break
  x = list(map(int, input().split()))
  for i in range(len(x)):
    if x[i] > 0 :
      x[i] = 1
    elif x[i] ==0 :
      x[i] = 0
    else:
      x[i] = -1
  
  for _ in range(k):
    order = list(input().rstrip().split())
    preorder = order[0]
    postorder = order[1:]

    if preorder == "P":
      sum = 1
      for i in range(int(postorder[0]), int(postorder[1]) + 1):
        sum *= x[i-1]
      if sum > 0:
        print("+",end="")
      elif sum == 0:
        print("0",end="")
      else:print("-",end="")
    else: 
      x[int(postorder[0]) - 1] = int(postorder[1])

  
  print()