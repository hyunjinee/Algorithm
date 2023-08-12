err = lambda:print("I'm Sorry Hansoo")

s = list(input())

s.sort()

d = {}

for i in s:
    if d.get(i) != None:
        d[i] += 1

    else: 
        d[i] = 1

print(d)
last = ''

for k,v in d.items():
    if (v % 2== 1 and last!= ''):
        err()
        exit(0)
    if v % 2 == 1:
        last = k

o = ""

for k, v in d.items():
    o += k * (v// 2)

print(o + last + o[::-1])