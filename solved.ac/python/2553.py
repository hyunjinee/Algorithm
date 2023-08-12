n = int(input())

s = [0 ] * (n + 1)
s[0] = 1
s[1] = 1

for i in range(2, n+1):
  s[i] = s[i-1] * i


if str(s[-1])[-1] == '0':
  print(str(s[-1])[-2])
else:
  print(str(s[-1])[-1])