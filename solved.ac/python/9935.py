
string = input()
bomb = input()

stack = []
for i in range(len(string)):
  stack.append(string[i])

  if len(stack) >= len(bomb):
    temp = ''.join(stack[-len(bomb): ])
    if temp == bomb:
      cnt = 0 
      while cnt < len(bomb):
        stack.pop()
        cnt += 1
      
if len(stack ) == 0:
  print("FRULA")
else: 
  print("".join(stack))
# string = input()
# bomb = input()

# while string.find(bomb) != -1:
#     string = string.replace(bomb, '')
    

# print(string if string else 'FRULA')