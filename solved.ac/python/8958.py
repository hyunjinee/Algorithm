N = int(input())

for i in range(N):
    
    answer = input()
    count =0
    sum=0
    
    if answer[0]=="O":
        count =1
        sum=1
        
    elif answer[0]=="X":
        count= 0
        
    for j in range(1,len(answer)):
        
        if answer[j]=="O":
            count +=1
        elif answer[j]=="X":
            count= 0
        sum+=count
    print(sum)   
