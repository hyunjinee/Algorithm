import sys
from collections import deque

q = deque()
stack = []


result = ''
state = True


str = list(sys.stdin.readline().strip())


for i in str:
    if i == '<':
        while stack:
            result += stack.pop()
        q.append(i)
        state = False
    elif i == '>':
        q.append(i)
        state = True

        while q: 
            result += q.popleft()
    
    elif i == ' ':
        if state:
            while stack:
                result += stack.pop()
            result += ' '
        else:
            q.append(i)
            while q:
                result += q.popleft()
    else:
        if state:
            stack.append(i)
        else:
            q.append(i)


while stack:
    result += stack.pop()

print(result)