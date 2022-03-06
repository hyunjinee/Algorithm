import sys
input = sys.stdin.readline


while True:

  s = input().rstrip().split()
  if s[0] == '*' : break
  temp =  s[0][0]
  flag = True
  for i in range(len(s)):
    if temp.upper() == s[i][0].upper():
      continue
    else:
      flag = False

  if flag:
    print("Y")
  else:
    print("N")