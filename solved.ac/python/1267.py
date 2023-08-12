N = int(input())
s = list(map(int,input().split()))
y = 0
m = 0
for i in s:
    y += i//30*10+10
    m += i // 60 * 15 + 15
if y < m:
    print('Y %d' % y)
elif y > m:
    print('M %d' % m)
else:
    print('Y M %d' % y)
