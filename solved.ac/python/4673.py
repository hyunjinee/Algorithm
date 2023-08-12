lst = [i for i in range(1,10000) ]
for j in range(1,10000):
    sumofall = j
    for k in range(len(str(j))):
        sumofall += int(str(j)[k])
    if sumofall in lst :
        lst.remove(sumofall)
    
for x in lst:
    print(x)