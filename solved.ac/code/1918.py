# 중위 표기식을 처음부터 순서대로 읽으면서 피연산자는 즉시 출력한다.
# 모든 연산자는 일단 스택에 푸쉬한다.
# 단 이때 스택내에 우선순위가 자신보다 더 높은 연산자가 있으면 pop하여 출력한 후에 push 한다.
# 수식이 종료되면 스택에 있는 모든 연산자를 pop하여 출력한다.

string = input()
stack = []
result = ''

for s in string : 
  if s.isalpha(): # 알파벳이면 결과에 넣어요~ 피연산자는 나오는 즉시 출력한다. 
    result += s
  else:
    if s == '(': # 여는 괄호 스택에 넣어요~
      stack.append(s)
    elif s == '*' or s == '/': # 곱하기나 나누기는 같은 우선순위에 있는 곱하기랑 나누기를 결과문자열에 추가한다.
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        result += stack.pop()
      stack.append(s)
    elif s == '+' or s == '-': # 연산자는 바로 출력할 수는 없다. 연산자는 적어도 뒤에 계산되는게 같이 나온다음에 출력할 수 있다.
      # 연산자는 스택에 넣어두자~! 피연산자는 출력하자~!
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