import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break
    
    small, capital, num, space = 0, 0, 0, 0

    for i in range(len(s)):

        if s[i].islower():
            small += 1

        elif s[i].isupper():
            capital += 1
        
        elif s[i].isdigit():
            num += 1

        else:
            space += 1

    print(small, capital, num, space)