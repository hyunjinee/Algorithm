



# # 수열이 정의되어있다.
# # D[1] = A
# # D[n] = D[n-1] 의 숫자 를 p 번 곱한수의 합


# # # 이과정을 반복하면 반복수열이된다?????

# # a, p = map(int, input().split())
# # d = []

# # d.append(a)

# # # 반복수열의 체크를 어떻게 할 것인가? 이게 포인트인거같은데..
# # # 

# # a = str(a)


# import sys a, p = map(int, sys.stdin.readline().split()) seq = [a] while True: t = seq[-1] val = 0 while t: val += ((t%10) ** p) t //= 10 if val in seq: sys.stdout.write(str(seq.index(val))) break else: seq.append(val)

# 출처: https://suri78.tistory.com/127 [공부노트]


import sys

a, p = map(int, sys.stdin.readline().split())
seq = [a]
while True:
    t = seq[-1]
    val = 0
    while t:
        val += ((t % 10) ** p)
        t //= 10

    if val in seq:
        # print(val)
        sys.stdout.write(str(seq.index(val)))
        break
    else:
        seq.append(val)
    # val 이 seq 에 있으면
