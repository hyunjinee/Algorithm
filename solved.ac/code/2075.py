# python3 메모리초과
# pypy3 시간 초과
import sys
input = sys.stdin.readline

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

ans = sorted(numbers[-1], reverse=True)

for i in range(N - 2, -1, -1):
    max_of_row = max(numbers[i])
    # print(max_of_row, min(ans))
    if max_of_row < min(ans):
        break
    else:
        for j in range(N):
            if numbers[i][j] > min(ans):
                ans.append(numbers[i][j])
        # print(ans)
ans.sort(reverse=True)
ans = ans[0: N]
# print(ans)
print(ans[-1])
