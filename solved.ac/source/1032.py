n = int(input())
s = list(input())
for i in range(n-1):
    new_ =  input()
    for j in range(len(s)):
        if s[j] == new_[j]:
            continue
        else:
            s[j] = "?"


print("".join(s))