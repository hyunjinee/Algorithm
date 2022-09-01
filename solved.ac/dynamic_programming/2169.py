import sys

# 재귀깊이 해제
sys.setrecursionlimit(100000)

# go : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 리턴하는 함수
def go(x, y, z):
    # Base Case : 오른쪽 아래에 도달한 경우
    if x == n - 1 and y == m - 1:
        return arr[x][y]
        
    # Memoization
    if dp[x][y][z] != -1:
        return dp[x][y][z]
        
    # 음의 무한대로 초기화
    dp[x][y][z] = -9876543210
    
    for i in range(3):
        # nx, ny : 다음 좌표
        nx, ny = x + dx[i], y + dy[i]
        
        # 오른쪽으로 왔다가 왼쪽으로 가는 경우, 왼쪽으로 왔다가 오른쪽으로 가는 경우는 continue
        if z == 1 and i == 2:
            continue
        if z == 2 and i == 1:
            continue
            
        # 범위 확인 및 점화식
        if 0 <= nx < n and 0 <= ny < m:
            dp[x][y][z] = max(dp[x][y][z], go(nx, ny, i) + arr[x][y])
    return dp[x][y][z]

# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx, dy : x좌표와 y좌표의 이동배열
dx = [1,0,0]
dy = [0,1,-1]

# dp : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 저장하는 상태 공간
dp = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

# 정답 출력
print(go(0,0,-1))