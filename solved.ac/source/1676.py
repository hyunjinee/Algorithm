N = int(input())

def factorial(N):
    if N < 2 :
        return 1
    else:
        return N * factorial(N-1)
numtostr = str(factorial(N))
i = len(numtostr)
count = 0
while i > 0:
    i-=1
    
    if numtostr[i] == "0" :
        count +=1
    if  numtostr[i] != "0":
        print(count)
        break
