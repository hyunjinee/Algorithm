A = input()
B = input()

LA = len(A)
LB = len(B)

prev = [0] * (LB + 1)
ans = 0

for i in range(LA):
    cur = [0] * (LB + 1)
    for j in range(LB):
        if A[i] == B[j]:
            cur[j + 1] = prev[j] + 1
    ans = max(ans, max(cur))
    prev = cur[:]
print(ans)