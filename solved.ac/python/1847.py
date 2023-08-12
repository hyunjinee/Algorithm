from sys import stdin
origin=[]
new=[]
result=['+']
for i in range(1,int(stdin.readline())+1):
    origin.append(int(stdin.readline()))
    new.append(i)
origin.append('end')
new.append('fin')
new.append('dummy')
o_p=0
n_p=0
while True:
    if origin[o_p]==new[n_p]:
        result.append('-')
        new.pop(n_p)
        o_p+=1
        n_p-=1
        if origin[o_p]=='end':break
    else :
        n_p += 1
        if new[n_p]=='fin':break
        result.append('+')
if len(new)==2:
    for i in result:
        print(i)
else:
    print('NO')