points = [list(map(int,input().split())) for _ in range(3)]


vec1 = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
vec2 = [points[2][0] - points[1][0], points[2][1] - points[1][1]]
func = (vec1[0]* vec2[1] - vec1[1] * vec2[0])
if func > 0:
  print(1)
elif func == 0 :
  print(0)
else: print(-1)
