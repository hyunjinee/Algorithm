s = input().split()

for i in range(len(s) - 1):
  if s[i] == s[i+1]:
    s.pop(s.index(s[i]))
  
print("".join(s))