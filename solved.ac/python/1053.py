import sys
input = sys.stdin.readline

def dfs(left, right):
    if left >= right:
        return 0
    if dp[left][right] == INF:
        # dfs(left+1, right-1) : 왼쪽이나 오른쪽 문자 교체
        # dfs(left, right-1) : 왼쪽에 삽입 or 오른쪽 문자 삭제
        # dfs(left+1, right) : 오른쪽에 삽입 of 왼쪽 문자 삭제
        dp[left][right] = min(dp[left][right], dfs(left+1, right-1)+int(origin[left]!=origin[right]), dfs(left, right-1)+1, dfs(left+1, right)+1)
    return dp[left][right]

if __name__ == '__main__':
    origin = list(input().strip())
    n = len(origin)
    INF = n+1
    dp = [[INF]*n for _ in range(n)]

    ans = dfs(0, n-1)

    for i in range(n):
        for j in range(i+1, n):
            dp = [[INF]*n for _ in range(n)]
            origin[i], origin[j] = origin[j], origin[i]
            ans = min(ans, dfs(0, n-1)+1)
            origin[i], origin[j] = origin[j], origin[i]
    print(ans)
