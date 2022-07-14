n, m = map(int, input().split())
coins = [list(str(input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        coins[i][j] = int(coins[i][j])
answer = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if coins[i][j] == 1:
            answer += 1
            for k in range(i+1):
                for l in range(j+1):
                    coins[k][l] = not coins[k][l]
        if coins == [[0 for _ in range(m)] for _ in range(n)]:
            print(answer)
            quit()