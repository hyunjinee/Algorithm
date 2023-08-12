def solve():
    N, A = int(input()), [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]
 
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1): # 부분 파일의 길이
        for j in range(1, N+2-i):   # 시작점
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
 
    print(DP[1][N])
 
for _ in range(int(input())):
    solve()


# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     n = int(input())
#     f = list(map(int,input().split()))
#     d = [[0]*(n+1) for i in range(n+1)]
    
#     for i in range(n-1):
#         d[i][i+1] = f[i] + f[i+1]
#         for j in range(i+2,n):
#             d[i][j] = d[i][j-1] + f[j]

#     for v in range(2,n):
#         for i in range(n-v):
#             j = i+v
#             d[i][j] += min([d[i][k] + d[k+1][j] for k in range(i,j)])
    
#     print(d[0][n-1])
  



# # 소설가 김대전은 소설을 여러장으로 나누어 쓰는데, 각장은 다른 파일에 저장하곤한다. 
# # 두개의 파일을 합쳐서 하나의 임시파일을 만들고 이 임시파일이나 원래의 파일을 계속 두개씩합쳐서 소설의 여러장들이 연속이
# # 되도록 파일을 합쳐나가고 최종적으로는 하나의 파일로 합친다.
# # 두개의 파일을 합칠때, 필요한 비용이 두파일 크기의 합이라고 할 때, 최종적인 한개의 파일을 완성하는데 필요한 
# # 비용의 총합을 계산하시오

# # 파일 합칠 때 최소 비용을 계산

# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#   k = int(input())
#   files = list(map(int,input().split()))
#   files.sort()
#   print(files)
#   ans = 0
#   while len(files) > 1:
#     files.sort()
#     temp = []
#     if len(files) % 2 == 0:
#       for i in range(0, len(files) - 1, 2):
#         temp.append(files[i] + files[i+1])
#     else:
#       for i in range(0 ,len(files) - 2, 2):
#         temp.append(files[i] + files[i+1])
#       temp.append(files[-1])
#     files = temp

#     for i in range(len(files)):
#       ans += files[i]

#     print(files, "파일")
#     print(ans)
  