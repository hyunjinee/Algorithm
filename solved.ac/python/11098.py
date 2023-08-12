
for i in range(int(input())):
    players = []
    for j in range(int(input())):
        price, name = input().split()
        price = int(price)
        players.append((price, name))
    players.sort(key = lambda player: player[0])
    print(players[-1][1])