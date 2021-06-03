import time

def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum +i
    end = time.time()
    return theSum, end-start

n =5 
print("총합계: %d\t 시간: %10.7f초" % sumOfN2(n))
n =220230
print("총합계: %d\t 시간: %10.7f초" % sumOfN2(n))