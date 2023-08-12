from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
a = [list(input()) for i in range(n)]

c = 0

for i in a:
     
    li = deque()
    for j in i:
        if len(li) == 0:
            li.append(j)
        elif len(li) >= 1:
            if li[-1] == j:
                li.pop()
            else:
                li.append(j)

    if len(li) == 0:
        c += 1
print(c)

# ABAB

# AABB