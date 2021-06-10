import sys
sys.stdin = open("input.txt", 'r')


h, w = map(int,input().split())

c = int(input())



wp = [0]
hp = [0]

max_w = 0
max_h = 0

for _ in range(c):
    data = input().split()


    if data[0] == '0':
        wp.append(int(data[1]))
    else:
        hp.append(int(data[1]))


wp.sort()
wp.append(w)
hp.sort()
hp.append(h)



for i in range(len(wp) -1):
    if max_w < wp[i+1] - wp[i]:
        max_w = wp[i+1] - wp[i]

for i in range(len(hp) - 1):
    if max_h < hp[i+1] - hp[i]:
        max_h = hp[i+1] - hp[i]




print(max_w * max_h


)