import sys
input = sys.stdin.readline

N,K = map(int,input().split())
dp =[[0]*(N+1) for _ in range(K+1)]
times=[]
grades=[]
for _ in range(K):
    I,T = map(int,input().split())
    times.append(T)
    grades.append(I)

for class_no in range(1,K+1):
    for now_time in range(1,N+1):
        if times[class_no-1] > now_time:
            dp[class_no][now_time] = dp[class_no-1][now_time]
        else:
            # 지금시간에서 추가하는 과목의 소요시간만큼 뺐을때의 누적가치+그 과목의 점수, 그냥 추가 안했을때 점수 중 높은값.
            dp[class_no][now_time] = max(grades[class_no-1]+dp[class_no-1][now_time-times[class_no-1]],
            dp[class_no-1][now_time])
print(dp[K][N])
# 0 1 냅색 