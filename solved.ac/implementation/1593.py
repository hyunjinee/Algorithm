g, s = map(int, input().split())
W = input()
S = input()

answer = 0
wa = [0] * 58
sa = [0] * 58

for x in W:
    wa[ord(x) - 65] += 1

# 구간 비교를 시작할 시작점 start와 현재 카운팅한 알파벳 길이 length를 초기화하고 시작한다.
start, length = 0, 0
for i in range(s):
    sa[ord(S[i]) - 65] += 1
    length += 1
    
    if length == g:
        if wa == sa:
            answer += 1
        sa[ord(S[start]) - 65] -= 1 # 이 코드를 통해 시간 복잡도를 줄일 수 있다
        start += 1
        length -= 1
    
print(answer)

