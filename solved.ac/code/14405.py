
s = input()
canDo = ["pi", "ka", "chu"]
for i in range(3):
  s = s.replace(canDo[i], "*")
for i in range(len(s)):
  if ord('a') <= ord(s[i]) <= ord('z'):
    print("NO")
    exit()
print("YES")
# for i in range(3):
#   temp = s.split(canDo[i])
#   s = ''.join(temp)
#   if not len(s) : 
#     print("YES")
#     sys.exit()
# print("NO")
