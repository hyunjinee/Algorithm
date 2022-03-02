s = input()
for c in ['a', 'e', 'i', 'o', 'u']:
    s = s.replace(c+'p'+c, c)
print(s)