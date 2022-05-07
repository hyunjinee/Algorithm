n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i * 2 <= n * 2 - i ** 2 + i and (n * 2 - i ** 2 + i) % (i * 2) == 0:
        cnt += 1
print(cnt)