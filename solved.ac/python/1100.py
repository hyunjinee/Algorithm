count =0
lines = []

for i in range(8):
    line = input()
    lines.append(line)
for k in range(8):
    if k%2==0:
        for i in range(8):
            if(i%2==0 and lines[k][i]=="F"):
                count+=1
    elif k%2==1:
        for j in range(8):
            if j%2==1 and lines[k][j]=="F":
                count+=1   


print(count)

