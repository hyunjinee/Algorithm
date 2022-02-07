#include <cstdio>
using namespace std;

#define MOD 9901

int main () 
{
  int N, i, ans;
  scanf("%d", &N);
  int dp[N+1][3];

  dp[1][0] = 1, dp[1][1] = 1, dp[1][2] = 1;
  for (i = 2; i<=N; i++) {
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD;
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD;
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD;
  }

  ans = (dp[N][0] + dp[N][1] + dp[N][2])  % MOD;
  printf("%d\n", ans);
  return 0;
}