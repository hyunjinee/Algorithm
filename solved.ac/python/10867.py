#입력
N = int(input())
number_list = list(map(int, input().split()))

#출력
for i in sorted(list(set(number_list))): #set으로 중복 방지, sorted로 정렬
    print(i, end = ' ')