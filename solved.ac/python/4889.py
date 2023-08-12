answer = []

while True:
    stack = []
    count = 0
    s = input()
    if '-' in s: # 종료 조건
        break
    for i in range(len(s)): 
        if not stack and s[i] == '}': # 스택에는 { 이 친구만 넣는다. 스택에  } 이거 들어오면 pop
            count += 1 # 스택에 } 가 처음들어오면 { 로 바꿔서 추가 그리고 카운트 증가
            stack.append('{')
        elif stack and s[i] == '}': # 스택이 있고 } 가 들어오면 { 를 팝
            stack.pop()
        else:
            stack.append(s[i]) # { <= 이친구는 무조건 추가 
    count += len(stack)//2 # 남는건 무조건 여는 괄호니까 여는 괄호의 반만 증가
    answer.append(count)

for i in range(len(answer)):
    print(i+1, '. ', answer[i], sep='')