
# s <= 150
# ( )~ 이렇게하면 안에꺼 무한 반복 가능
# ( | )~ 이렇게하면 둘중하나로 무한 반복가능
# 무조건 정규 표현식인데




import re

s = input()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")