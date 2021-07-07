# 수열 하나를 가진다.  수열을 정열적으로 정렬하려고한다. 
# ㅋㅋ

# 첫째 줄에 수열의 길이 N 이 주어진다. 
# 둘째 줄에 수열의 각 원소 a가 공백을 두고 차래대로 주어진다.


n = int(input())

lst = list(map(int,input().split()))


lst.sort()


print(*lst)