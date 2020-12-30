i = int(input())

list=[0]*(i+2)
list[1]=1
for i in range(2,i+2):
    list[i] = list[i-1]+list[i-2]
print(list[i-1])


