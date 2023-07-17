import sys

a,b = map(int,sys.stdin.readline().split())

case = int(sys.stdin.readline())
arr=[]
for i in range(case):
    arr.append(int(sys.stdin.readline()))

sum1 = abs(b-a)

for i in range(case):
    arr[i] = abs(b-arr[i])

sum2=min(arr)

print(min(sum1,sum2+1))