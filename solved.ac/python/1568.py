n = int(input())


count = 1 

time = 0
while True:
    if count > n:
        count = 1

    n = n - count


    count += 1


    time += 1


    if n == 0: break

print(time)