N = int(input())
lst =[]
for i in range(N):
    num = int(input())
    lst.append(num)

lst.sort()
lst.reverse()

for number in lst:
    print(number)