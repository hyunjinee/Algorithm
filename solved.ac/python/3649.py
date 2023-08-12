import sys; input = sys.stdin.readline

while True:
  try:
    x = int(input()) * 10000000
    n = int(input())

    legos = [int(input()) for _ in range(n)]
    legos.sort()

    i, j = 0 , n -1

    flag = True

    while i < j : 
      if legos[i] + legos[j] == x:
        print('yes %d %d' % (legos[i], legos[j]))
        flag = False
        break
      elif legos[i] + legos[j]  < x:
        i += 1

      else:
        j -= 1

    if flag:
      print('danger')

  except:
    break