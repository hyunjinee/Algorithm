import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())

bottle = defaultdict(int)
bottle[1] = N

liter, buy = 1, 0
while 1:
    while liter in bottle: 
        #해당 liter을 가진 물병이 1병 이상 존재할 때, 합칠 수 있을 만큼 합침
        if bottle[liter] > 1:
            bottle[liter * 2] += bottle[liter] // 2
            bottle[liter] %= 2
        liter *= 2 
        
    if sum(list(bottle.values())) <= K: #총 가지고 있는 물병의 양이 K개 이하일 경우 반복문 종료
        break

    #합칠 수 있는 최소 물병의 수를 구입
    liters = [liter for liter in bottle if bottle[liter] > 0]
    buy += liters[1] - liters[0]
    bottle[liters[0]] = 0
    bottle[liters[1]] = 0
    bottle[liters[1] * 2] += 1
    liter = liters[1] * 2
        
print(buy)