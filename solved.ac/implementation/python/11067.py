import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):   
    n = int(input())    
    answer = [[0, 0]]
    dic = {}
    
    for j in range(n):
        x, y = map(int, input().split())
        if x not in dic:
            dic[x] = list()
        dic[x].append(y)

    # print(dic)
        
    sdic = sorted(dic.items())

    print(sdic)

    for j in range(len(sdic)):
        sdic[j][1].sort()
        if answer[-1][1] != sdic[j][1][0]:
            sdic[j][1].sort(reverse = True)   
        for k in range(len(sdic[j][1])):
            answer.append([sdic[j][0], sdic[j][1][k]])
            
    m = list(map(int, input().split()))

    for j in range(1, len(m)):
        print(*(answer[m[j]]))