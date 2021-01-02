T = int(input())
for i in range(T):
    R, S = map(str, input().split())

    word = ""
    for s in S:
        word = word + s*int(R)
    print(word)