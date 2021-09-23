x = int(input())

total = 64
count = 0 


sticks = [64]



while total > x:
    
    find = sticks.index(min(sticks))    
    popped = sticks.pop(find)
    sticks.append(int(popped/2))
    # 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면,
    if sum(sticks) >= x:
        pass
    else :
        sticks.append(int(popped/2))
    total = sum(sticks)
    # print(sticks)
    
print(len(sticks))
# 몇개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 출력한다.