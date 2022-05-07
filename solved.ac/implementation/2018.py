N = int(input())
start = 0 #첫 숫자
end = 1 #끝 숫자
answer = 0 #정답
sum_numbers = 1 #답이 되는 숫자

while start < N//2 + 1:
    if sum_numbers < N: #작을 경우 뒤에 숫자 하나를 더붙여줌
        end += 1
        sum_numbers += end
    elif sum_numbers == N: #맞을 경우 숫자 answer += 1
        answer += 1
        end += 1
        sum_numbers -= start
        sum_numbers += end
        start += 1
    else: #클 경우 앞에 숫자 하나를 없애줌
        sum_numbers -= start
        start += 1
        
print(answer + 1) #자기 자신 + 1