N = int(input())
position =[]
for i in range(N):
    x,y = map(int, input().split())
    position.append((x,y))
position.sort()
for x in range(N):
    for y in range(2):
        print(position[x][y], end=" ")
        
    print()