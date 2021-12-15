import sys
input = sys.stdin.readline

def cnt (n) :
  if n == 0 or n== 1:
    return 1

  a = [0 for _ in range(n+1)]
  a[0],a[1] = 1,1
  for i in range(2, n+ 1):
    a[i] = a[i-1] + 2 * a[i -2]
  return a[n]


while True:
  try:
    print(cnt(int(input())))
  except:
    break

