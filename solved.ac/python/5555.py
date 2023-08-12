# 여기서한 4시쯤나가?


# 입력은 2 + N 줄이다.

# 첫번째 줄에는 1자이상 10자이하의 대문자로 구성된 찾고자 하는 문자열

find = input()

count = int(input())
ans = 0
for i in range(count):


    banzi = input()
    banzi = banzi + banzi
    if find in banzi:
        ans += 1

    
print(ans)