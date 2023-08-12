N,X = map(int, input().split())

keep =[]
numbers = list(map(int, input().split()))
for num in numbers:
    if(num <X):
        num = str(num)
        keep.append(num)

print(' '.join(keep))
