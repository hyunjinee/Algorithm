import sys
from itertools import combinations

n = list(map(str, sys.stdin.readline().strip()))
answer = set()
stack = []
temp = []

# 반복문을 통해 괄호의 시작점과 끝점을 저장
for idx, word in enumerate(n):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        temp.append((stack.pop(), idx))

for i in range(1, len(temp) + 1):
    c = combinations(temp, i) # combinations을 통해 모든 경우의 수를 확인

    # 반복문을 통해 경우의 수를 확인
    for j in c:
        target = list(n)

        # 괄호 제거
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""

        answer.add(''.join(target))

for ans in sorted(list(answer)):
    print(ans)