import sys
input = sys.stdin.readline
ship = []
for _ in range(int(input())):
    x = int(input())-1
    if x:
        for i in ship:
            if x%i==0:
                break
        else:
            ship.append(x)
print(ship)
print(len(ship))