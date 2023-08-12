K, N = map(int, input().split())
cm =[]
for i in range(K):
    cm.append(int(input()))

for i  in range(sum(cm)//11 , 0 , -1):
    if cm[0]//i + cm[1]//i + cm[2]//i + cm[3]//i == N:
        print(i)
        break

# 시간 초과 남 비효율적이야 너무 ㅡㅡ