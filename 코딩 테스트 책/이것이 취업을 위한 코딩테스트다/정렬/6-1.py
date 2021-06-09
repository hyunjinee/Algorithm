array= [ 7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

        array[i], array[min_index] = array[min_index] , array[i]


print(array)




# 선택 정렬은  n- 1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야한다.
# 또한 매번 가장 작은 수를 찾기 위해서 비교연산이 필요하다.
# 구현 방식에 따라서 사소한 오차는 있을 수 있지만 앞쪽의 그림대로 구현했을 때 연산횟수는 ..



# 삽입 정렬에서는 특정한 데이터가 삽입될 위치를 선정할 때 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면 된다.



for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j] , array[j-1] = array[j-1], array[j]

        else: break



# 퀵정렬과 병합 정렬은 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이다.


