li = [0, 1, 2]
x, y = map(int, input().split())
d = y - x

if d <= 2:
    print(li[d])
else:
    i = 2
    while True:
        if i * (i - 1) < d <= i * i:
            print(2 * i - 1)
            break
        elif i * i < d <= i * (i + 1):
            print(2 * i)
            break
        i += 1