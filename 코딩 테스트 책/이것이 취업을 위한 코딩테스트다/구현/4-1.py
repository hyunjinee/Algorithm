n= int(input())

cur_pos = [1, 1]
# print(cur_pos[0], "안녕ㅋ")
p = list(input().split())
# print(p)
for i in range(len(p)):
    if p[i] == "R" and cur_pos[1] + 1 <= n:
        cur_pos[1] += 1
    elif p[i] == "L" and cur_pos[1] - 1 >= 1:
        cur_pos[1] -= 1
    elif p[i]== "U" and cur_pos[0] - 1  >= 1: 
        cur_pos[0] -= 1
    elif p[i] == "D" and cur_pos[0] + 1 <= n:
        cur_pos[0] += 1

    
print(cur_pos)



# 최종적으로 도착할 지점의 좌표를 공백으로 구분하여 출력한다.

# RRRUDD 
# 생각을 해보자
# 현재 좌표는 1 1이고 오른쪽 끝아래 좌표는 n n이다.
# 또한 그 움직임에 대한 검사를 하는 함수가 필요하다.

# def check_move(x,y):
#     if 1 <= x <= n and 1 <= y <= n:
#         return True
#     else: return False
