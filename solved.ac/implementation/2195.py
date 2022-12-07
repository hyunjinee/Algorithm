s = input()
p = input()
ans, idx = 0, 0

while idx < len(p):
  copy = ''

  if s.find(p[idx:]) != -1:
    ans += 1
    break

  for j in range(idx, len(p)):
    copy += p[j]
    if s.find(copy) == -1:
      ans += 1
      idx = j
      break

print(ans)