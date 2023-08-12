s = input()

a  = ''
i = 0
while i <= len(s) - 1:
  if s[i] in ['a', 'e', 'i', 'o', 'u']:
    a += s[i]
    i += 2
  else: 
    a += s[i]

  i += 1

print(a)