s = input()
res = ''
for c in s:
    if 'a' <= c <= 'z':
        res += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        res += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        res += c
print(res)