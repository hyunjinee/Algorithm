# 배열 두개를 가지고있다 두 배열은 n개의 원소로 구서오디어있다.
# 배열의원소는 모두 자연수이다.동빈이는 최대 k번의 바꿔치기 연산을 수행 할 수 있는데, 바꿔치기 연산이란 배열 A에있는 원소하나와
#qodufb에ㅣㅇㅆ는 원소를 바꾸는 것이다.


# n 개의 원소
# k 번의 바꿔치기




# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
# 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램


# 배열 a와b의 정보가 입력되면 배열의 원소를



n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


a.sort()
b.sort(reverse=True)

for i in range(k):

    if a[i] < b[i]:
        a[i],b[i] = b[i], a[i]
    else:
        break

print(sum(a))
