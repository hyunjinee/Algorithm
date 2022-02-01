n = int(input())

def isyun(x):

  if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    return True
  else:
    return False


if isyun(n):
  print(1)
else: 
  print(0)