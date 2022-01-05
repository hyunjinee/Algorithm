string = input()
stack = []
result = ''

for s in string : 
  if s.isalpha(): # 알파벳이면 스택에 넣어요~
    result += s
  else:
    if s == '(': # 여는 괄호 또한 스택에 넣어요~
      stack.append(s)
    elif s == '*' or s == '/': # 곱하기나 나누기는 같은 우선순위에 있는 곱하기랑 나누기를 결과문자열에 추가한다.
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        result += stack.pop()
      stack.append(s)
    elif s == '+' or s == '-':
      while stack and stack[-1] != '(' :
        result += stack.pop()
      stack.append(s)
    elif s == ')':
      while stack and stack[-1] != '(':
        result += stack.pop()

      stack.pop()

while stack : 
  result += stack.pop()

print(result)