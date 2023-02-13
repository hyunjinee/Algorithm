n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    L = A[:]

    press = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 pass

        if L[i-1] == B[i-1]:
            continue
        # 상태가 다를 경우

        press += 1
        for j in range(i-1, i+2):
            if j<n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9


# 첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우

print(bulb)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
print(bulb, target)
res = min(res, change(bulb, target) + 1)
print(res if res != 1e9 else -1)