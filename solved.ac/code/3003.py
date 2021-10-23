# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때 , 몇개를 더하거나 빼야 올바른 세트가 되는지

# 동혁이가 찾은 흰색 킹 , 퀸, 룩, 비숍, 나이트 ,폰
cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i], end=' ')