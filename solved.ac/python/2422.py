


# 3 가지 
n, m = map(int, input().split())


cnt = 0


if n < 3:
    print(cnt)


else:

    unmixed = {i: [] for i in range(1, n+1)}
    for _ in range(m):

        i, j = map(int, input().split())

        unmixed[i].append(j)

        unmixed[j].append(i)

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, n+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)





