bugers = []
bevs= []
for i in range(5):
    if i<3:
        buger = int(input())
        bugers.append(buger)
    else:
        bev = int(input())
        bevs.append(bev)

print(min(bugers)+min(bevs)-50)
