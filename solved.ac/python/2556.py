
max_num = 0

for i in range(9):
    row = list(map(int, input().split())) #굳이 행렬을 저장할 필요는 없다
    if max(row) > max_num:
        max_num = max(row) #최댓값
        x = i + 1 #행
        y = row.index(max_num) + 1 #열
print(max_num)
print(x,y)