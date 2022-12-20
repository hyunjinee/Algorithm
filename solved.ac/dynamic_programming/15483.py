s1 = input()
s2 = input()

s1_size = len(s1)
s2_size = len(s2)

d = [[0] * (s2_size + 1) for _ in range(s1_size + 1)]

for i in range(s1_size + 1):
  d[i][0] = i
for i in range(s2_size + 1):
  d[0][i] = i

for i in range(1, s1_size + 1):
  for  j in range(1, s2_size + 1):
    if s1[i - 1] == s2[j - 1]:
      d[i][j] = d[i - 1][j - 1]
    else:
      d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1

print(d[s1_size][s2_size])