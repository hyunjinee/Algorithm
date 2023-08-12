n = int(input())

sum = 0
i = 1
while i <= n :
    
    if i %2 == 1 :
        sum = sum +1
        
    else: 
        
        count = 0
        for j in range(1, i+1):
            if j**2 == i:
                count = count +1
            if i % j == 0 :
                count = count +1
       
        count = count // 2
        
        sum = sum + count
        
    i = i+1
print(sum)
        # count = 0
        # j = 1
        # while j <= n:
        #     if j**2 == n:
        #         count +=1
        #     if n % j ==0:
        #         count +=1
        #     j= j+1
        
        # count = count // 2
        
        # sum = sum + count
        
    #     print(sum)
# print(sum)