p=[0,1,1]+[0]*98
for i in range(98):p[i+3]=p[i]+p[i+1]
for i in range(int(input())):print(p[int(input())])