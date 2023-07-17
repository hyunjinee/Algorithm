def sol(idx):
    global result
    if idx == len(S):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx+j]:
                    break
            else:
                sol(idx+len(A[i]))
    return
    
S = input()
A = []
dp = [0] * 101
for _ in range(int(input())):
    A.append(input())
result = 0
sol(0)
print(result)