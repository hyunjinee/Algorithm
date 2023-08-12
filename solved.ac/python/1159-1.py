import sys
line = sys.stdin.readline().split("\n")[0]
players = []

for i in range(int(line)):
    players.append(sys.stdin.readline().split("\n")[0])
# print(players)
p = dict()
for player in players:
    p[player[0]] = 0

for player in players:
    p[player[0]] +=1
letsgo = []
for key in p:
    if p[key] > 4:
        letsgo.append(key)

letsgo.sort()

if len(letsgo) >0:

    for x in letsgo:
        print(x,end="")
else:
    print("PREDAJA")