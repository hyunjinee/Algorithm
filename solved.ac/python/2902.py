s = input()
ans = ""
for substring in s.split("-"):
    ans+=substring[0]
print(ans)