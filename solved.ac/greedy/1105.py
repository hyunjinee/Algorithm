l, r = input().split()

l_len, r_len = len(str(l)), len(str(r))
cnt = 0

if l_len != r_len:
  print(cnt)
else:
  for i in range(r_len):
    if l[i] != r[i]:
      break
    else:
      if l[i] == '8':
        cnt += 1
  print(cnt)