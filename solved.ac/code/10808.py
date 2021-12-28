s = input()
alpha = [0] * 26
for l in s:
  alpha[ord(l) - ord('a')] += 1

print(*alpha)