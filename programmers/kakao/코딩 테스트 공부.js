function solution(alp, cop, problems) {
  let max_alp = 0
  let max_cop = 0
  problems.forEach((prob) => {
    max_alp = Math.max(prob[0], max_alp)
    max_cop = Math.max(prob[1], max_cop)
  })

  if (max_alp <= alp && max_cop <= cop) return 0

  //초기 알고력, 코딩력이 높아 배열 밖으로 튀어나가는거 맥스치로 고정
  alp = alp >= max_alp ? max_alp : alp
  cop = cop >= max_cop ? max_cop : cop

  let dp = Array.from(Array(max_alp + 2), () =>
    Array(max_cop + 2).fill(Infinity)
  )
  dp[alp][cop] = 0

  for (let i = alp; i <= max_alp; i++) {
    for (let j = cop; j <= max_cop; j++) {
      //현재 위치에서 1시간씩 공부한 최소비용 계산
      dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1)
      dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1)

      //현재 위치에서 각 문제별 공부한 최소비용 계산
      for (const problem of problems) {
        const [alp_req, cop_req, alp_rwd, cop_rwd, cost] = problem
        // 요구치를 넘겨 문제를 풀 수 있을 때
        if (i >= alp_req && j >= cop_req) {
          //각 알고력, 코딩력 별 맥스치를 초과하는 경우 최종칸만 갱신
          if (i + alp_rwd > max_alp && j + cop_rwd > max_cop) {
            dp[max_alp][max_cop] = Math.min(
              dp[max_alp][max_cop],
              dp[i][j] + cost
            )
            //알고력 초과
          } else if (i + alp_rwd > max_alp) {
            dp[max_alp][j + cop_rwd] = Math.min(
              dp[max_alp][j + cop_rwd],
              dp[i][j] + cost
            )
            //코딩력 초과
          } else if (j + cop_rwd > max_cop) {
            dp[i + alp_rwd][max_cop] = Math.min(
              dp[i + alp_rwd][max_cop],
              dp[i][j] + cost
            )
            //일반 케이스
          } else {
            dp[i + alp_rwd][j + cop_rwd] = Math.min(
              dp[i + alp_rwd][j + cop_rwd],
              dp[i][j] + cost
            )
          }
        }
      }
    }
  }

  return dp[max_alp][max_cop]
}
