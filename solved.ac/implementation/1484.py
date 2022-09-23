if __name__== '__main__':
    G = int(input())
    P = [x for x in range(1, 100001)]
    Q = [x for x in range(1, 100001)]

    N, M = 100000, 100000
    left, right = 0, 0 # 투 포인터
    ans = []
    while left < N and right < M:
        # G는 현재 몸무게(A)의 제곱 - 성원이가 기억하고 있던 몸무게(B)의 제곱
        # G = A^2 - B^2 => (A + B)*(A - B)
        tmp = (P[left] + Q[right]) * (P[left] - Q[right])
        if tmp == G: ans.append(P[left])
        if tmp < G:
            left += 1
            continue
        right += 1
    if not ans: print(-1)
    else:
        for y in ans: print(y)