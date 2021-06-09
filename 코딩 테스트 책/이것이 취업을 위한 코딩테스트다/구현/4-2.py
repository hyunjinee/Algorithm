n = int(input())



# 만약 3시면 3이 모두 포함되는거 아닝교
# 시 분 초 를 각각 리스트로 먹여야되는건가?
# 생각을 해보자
# 흠...일단 시에 3이 포함되면 ?
# 0 ~ 23 시가 있자나? 근데 그럼 3이 포함되는 시간은
# 3 시 13 시 23 시 밖에없네?
# 분은? 3 13 23 33 43 53 
# 초는 3 13 23 33 45 53
# 약간 힘든데 이렇게하니까? ㅋㅋㅋ
# 00시 00 분 00 초 에서
# 


h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)