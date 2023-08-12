arr = ["" for _ in range(15)]
for _ in range(5):
  s = input()
  for c in range(len(s)):
    arr[c] += s[c]
for s in arr:
  print(s, end="")