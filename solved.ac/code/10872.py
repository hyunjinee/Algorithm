n = int(input())

l = [1, 1, 2]
for i in range(3, n + 1):
    l.append(l[-1] * (i))

if n == 0 :
  print(1)
elif n == 1: 
  print(1)
else:
  # print(l)
  print(l[n])