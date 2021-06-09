# 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어있다. 이수를 큰 수부터 작은순으로 정렬해야한다.
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오..




n = int(input())



array = []


for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)


for i in array:
    print(i, end=' ')
    

