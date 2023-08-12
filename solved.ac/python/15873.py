N = input()

if(len(N)==4):
    print(20)
elif(len(N)==3):
    if(int(N[-1]) ==0):
        print(10+int(N[0]))
    else:
        print(10+int(N[-1]))
elif(len(N)==2):
    print(int(N[0])+int(N[1]))