import sys
input = sys.stdin.readline

if __name__ == "__main__":
    d, k = map(int, input().split())

    a, b = 1, 1 # 3부터 시작하니까 뭐...
    for _ in range(4, d + 1):
        a, b = b, a + b

    # print(a, b)
    
    ac = 1
    bc = 0
    while True:
        tmp = k - a * ac
        if tmp < 0:
            break

        if tmp % b == 0:
            bc = tmp // b
            break

        ac += 1

    print(ac)
    print(bc)
