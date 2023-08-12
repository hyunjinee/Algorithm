import re

N = int(input())
string= []
for _ in range(N):
    string.append(input())

for i in string:
    p=re.compile('(100+1+|01)+')
    result=p.fullmatch(i)
    if result:
        print('YES')
    else:
        print('NO')