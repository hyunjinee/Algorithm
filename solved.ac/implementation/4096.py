import sys
input = sys.stdin.readline

def isPalin(x):
  if x == x[::-1]:
    return True
  return False


while True:
  temp = input().rstrip()
  count = 0

  if temp == '0':break

  while True: 
    if isPalin(temp):
      print(count)
      break
    count += 1

    length = len(temp)
    temp = str(int(temp) + 1)

    if length > len(temp):
      rest = length - len(temp)
      temp = '0' * rest + temp

    
