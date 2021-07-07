names = input()
name_cnt = [0 for _ in range(26)]
# 입력을 받고 알파벳의 개수는 26개인것을 이용해 개수를 센다.
for name in names:
    name_cnt[ord(name) - 65] += 1
# 아스키코드를 이용해서 65갔다가빼고 몇개있는지 세세욤
odd = 0
odd_alpha = ''
alpha= ''



for i in range(26):
    if name_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i + 65)

    alpha += chr(i + 65) * (name_cnt[i] // 2)


# 위 포문은 일단 홀수개인것은 저장해놓고
# 짝수개인것은 반개만 더해놓고 홀수가 한개면 가능 홀수가 여러개면 펠린드롬이 불가능하다.



if odd > 1:
    print("I 'm Sorry Hansoo")
else:
    print(alpha + odd_alpha + alpha[::-1])

# 위와 같은 식으로 결과 도출