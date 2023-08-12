# n to m 


t = int(input())


for i in range(t):
    count = 0
    a,b = map(int,input().split())
    for j in range(a,b+1):
        


        if "0" in str(j):
            count += str(j).count("0")

    print(count)