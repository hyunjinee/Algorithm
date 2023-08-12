A,B = map(str, input().split())

cnts = list()

for i in range(len(B)- len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if(A[j] != B[j+i]):
            cnt +=1
    cnts.append(cnt)

print(min(cnts))