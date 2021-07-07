

# 숫자를 섞어서 30의배수를 만드는데 가장큰 30의 배수

# 만들수 없으면 -1 출력 

# 30 60 90 120 150 180 
# 210 240 270 300 330 360
# 390 420 450 480 510 540

n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))