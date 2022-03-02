import re
n = []
for _ in range(int(input())):
  l = re.findall('[0-9]+', input())
  for i in l:
    n.append(int(i))
n.sort()
for i in n :
  print(i)