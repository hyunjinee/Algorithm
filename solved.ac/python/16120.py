s = input()
ppap = ["P", "P", "A", "P"]
stack = []

for i in range(len(s)):
  stack.append(s[i])
  while len(stack) >=4 and stack[-4: ] == ppap:
    for _ in range(4):
      stack.pop()
    stack.append("P")
print("PPAP") if stack == ["P"] else print("NP")