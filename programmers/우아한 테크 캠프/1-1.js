// prettier-ignore
function solution(weights, head2head) {
  const answer = []
  const  players = []

  for (let i = 0; i < weights.length; i++) {
    const player = {
      num: i + 1,
      weight: weights[i],
      winCount: 0,
      heavyWinCount: 0,
      loseCount: 0,
      percent: 0,
    }

    for (let j = 0; j < head2head[i].length; j++) {
      if (head2head[i][j] === "W") {
        if (weights[j] > weights[i]) {
          player.heavyWinCount++
          player.winCount++
        } else {
          player.winCount++
        }
      } else if (head2head[i][j] == "L") player.loseCount++
    }

    if (player.winCount === 0 && player.loseCount === 0) player.percent = 0
    else
      player.percent =
       ( (player.winCount / (player.winCount + player.loseCount)) * 100 ) .toFixed(2)
      
    players.push(player)
  }
 console.log(players)
  players.sort((a,b) => a.percent - b.percent ? 1: (a.heavyWinCount - b.heavyWinCount) ? 1 : (a.weight - b.weight) ? 1: -1)
  players.map(player=> console.log(player.num))
  // players.map((player) => answer.push(player.num))
  // console.log(answer)
}

// solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]) // result [3,4,1,2]
// solution([145, 92, 86], ["NLW", "WNL", "LWN"]) // result [2,3,1]
// solution([60, 70, 60], ["NNN", "NNN", "NNN"]) // result [2,1,3]
function sortFunction(a, b) {
  if (a[0] == b[0]) {
    if (a[1] == b[1]) {
      if (a[3] == b[3]) {
        return a[2] - b[2]
      } else {
        return b[3] - a[3]
      }
    } else {
      return b[1] - a[1]
    }
  } else {
    return b[0] - a[0]
  }
}
