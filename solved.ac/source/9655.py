N = int(input())
count =1
if N ==1:
    print("SK")
elif N==2:
    print("CY")
elif N==3:
    print("SK")
else:
    while N - count >=3 :
            count +=1
    if count % 2 == 0:
        print("CY")
    else:
        print("SK")