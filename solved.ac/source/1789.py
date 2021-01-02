# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# input 200  output 19

S = int(input())
if S == 1:
    print(1)
else:
    sum = 0
    for s in range(S+1):
        sum += s
        if (sum > S):
            print(s -1)
            break
        elif(sum == S):
            print(s)
            break
#여기서 20까지 더할때 210 이되고 19까지 더할때는 190 일꺼잖아 그니까 200 을 만들기위해 최대로 숫자를 쓰려면 19인거야