f = open("C:/Users/hyunjin/Desktop/Algorithm/solved.ac/source/dev/stdin", "r", encoding='utf-8')
line = f.readline().split("\n")[0]
players = []

for i in range(int(line)):
    players.append(f.readline().split("\n")[0])
# print(players)
p = dict()
for player in players:
    p[player[0]] = 0

for player in players:
    p[player[0]] +=1
letsgo = ""
for key in p:
    if p[key] > 4:
        letsgo += key
print(letsgo)
    # print(key)
# print(p.values())
# print(p)    
f.close()