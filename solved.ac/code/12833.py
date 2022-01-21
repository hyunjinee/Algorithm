a,b,c=map(int, input().split())
for i in range(c%2):a^=b
print(a)