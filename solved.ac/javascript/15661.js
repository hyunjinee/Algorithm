const [N, ...S] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((input, i) => (i === 0 ? +input : input.split(" ").map(Number)))
const visited = Array(N).fill(false)
let min = Number.MAX_SAFE_INTEGER

const calculateMinScore = () => {
  let startTeamScore = 0
  let linkTeamScore = 0
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      // 조합에 쓰인 사람을 visited 배열로 판단해 startTeam 능력치에 합산.
      // 쓰이지 않았다면 linkTeam 능력치에 합산한다.
      if (visited[i] && visited[j]) startTeamScore += S[i][j] + S[j][i]
      if (!visited[i] && !visited[j]) linkTeamScore += S[i][j] + S[j][i]
    }
  }
  min = Math.min(Math.abs(startTeamScore - linkTeamScore), min)
}

const combination = (idx, cnt) => {
  // 각 팀의 스코어의 차이 계산 후 min 업데이트
  if (cnt >= 1) calculateMinScore()
  // 사람들의 조합을 모두 검사
  for (let i = idx; i < N; i++) {
    if (!visited[i]) {
      visited[i] = true
      combination(i + 1, cnt + 1)
      visited[i] = false
    }
  }
}

combination(0, 0)
console.log(min)

// const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

// const n = +input[0],
//   points = input.slice(1).map((e) => e.split(" ").map(Number))
// const visited = Array(n).fill(false)

// let diff = Infinity

// dfs([])

// function dfs(team) {
//   if (team.length === n) {
//     return
//   }

//   if (team.length >= 1 && team.length < n) {
//     const teamA = team
//     const teamB = []
//     for (let i = 1; i < n; i++) {
//       if (!teamA.includes(i)) {
//         teamB.push(i)
//       }
//     }
//     let teamAScore = 0
//     let teamBScore = 0
//     for (let i = 0; i < teamA.length; i++) {
//       for (let j = 0; j < teamA.length; j++) {
//         if (i === j) continue
//         teamAScore += points[teamA[i]][teamA[j]]
//       }
//     }

//     for (let i = 0; i < teamB.length; i++) {
//       for (let j = 0; j < teamB.length; j++) {
//         if (i === j) continue
//         teamBScore += points[teamB[i]][teamB[j]]
//       }
//     }

//     // const teamAScore = teamA.reduce((acc, cur) => {
//     //   return acc + points[cur].reduce((acc, cur) => acc + cur, 0)
//     // }, 0)

//     // const teamBScore = teamB.reduce((acc, cur) => {
//     //   return acc + points[cur].reduce((acc, cur) => acc + cur, 0)
//     // }, 0)

//     diff = Math.min(diff, Math.abs(teamAScore - teamBScore))
//   }

//   for (let i = 1; i < n; i++) {
//     if (!visited[i]) {
//       visited[i] = true
//       team.push(i)
//       dfs(team)
//       team.pop()
//       visited[i] = false
//     }
//   }
// }

// console.log(diff)
