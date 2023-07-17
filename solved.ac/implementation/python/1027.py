n = int(input())
buildings = list(map(int,input().split()))
ans = 0

def calc(x1,y1,x2,y2):
    return (y2-y1) / (x2-x1)
for index, building in enumerate(buildings):
  view_max = 0
  left_max = int(1e9)
  right_max = -int(1e9)
  for i in range(index - 1, -1, -1):
    c = calc(index + 1, building, i+1, buildings[i])
    if c < left_max:
      left_max = c
      view_max += 1
  for i in range(index + 1, n):
    c = calc(index + 1, building, i+1, buildings[i])
    if c > right_max:
      right_max = c
      view_max += 1
  ans  = max(ans, view_max)
print(ans)
# result = 0

# for index, building in enumerate(buildings):
#   right = index + 1
#   cur_slope_right = None
#   visible_right = 0
#   for index2 in range(right, n + 1):
#     if index2 == n: break
#     x2 = index2 + 1



# def slope(x1, y1, x2, y2):
#     return (y2 - y1) / (x2 - x1)
 
# N = int(input())
 
# buildings = list(map(int, input().split()))
 
# result = 0
# for i1, y1 in enumerate(buildings):
#     x1 = i1 + 1
#     # 오른쪽 볼 수 있는 빌딩 수
#     cur_slope_right = None
#     visible_right = 0
#     for i2 in range(i1+1, N+1):
#         if i2 == N: break
#         x2 = i2 + 1
#         y2 = buildings[i2]
#         slope_right = slope(x1, y1, x2, y2)
#         # print("RIGHT:", x1, y1, x2, y2, slope_right)
#         if cur_slope_right is None or cur_slope_right < slope_right:
#             cur_slope_right = slope_right
#             visible_right += 1
#     # print("visible_right:", visible_right)
 
#     # 왼쪽 볼 수 있는 빌딩 수
#     cur_slope_left = None
#     visible_left = 0
#     for i3 in range(i1-1, -1, -1):
#         if i3 == -1: break
#         x2 = i3 + 1
#         y2 = buildings[i3]
#         slope_left = slope(x1, y1, x2, y2)
#         # print("LEFT:", x1, y1, x2, y2, slope_left)
#         if cur_slope_left is None or cur_slope_left > slope_left:
#             cur_slope_left = slope_left
#             visible_left += 1
#     # print("visible_left:", visible_left)
 
#     if (visible_left + visible_right) > result: result = visible_left + visible_right
 
# print(result)