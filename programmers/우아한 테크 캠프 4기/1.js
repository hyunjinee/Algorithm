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

function solution(weights, head2head) {
  // 복서들의 몸무게 weights, 복서 선수들의 전적을 나타내는 head2head
  // 승률이 높은 복서의 번호가 앞으로 간다. 아직 다른 복서와 붙어본적이 없으면 0으로 취급한다.
  // 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞으로 간다.
  // 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서들의 번호들 중에는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 간다.
  // 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 간다.

  // 어떻게 접근할 것인가?

  const howManyBoxers = weights.length
  const boxersInfo = Array.from({ length: howManyBoxers }, () => [])

  for (let i = 0; i < howManyBoxers; i++) {
    let winCount = 0,
      loseCount = 0,
      winBiggerBoxer = 0,
      gameCount = 0

    for (let j = 0; j < howManyBoxers; j++) {
      if (head2head[i][j] == "L") {
        // 진 경우
        loseCount++
        gameCount++
      } else if (head2head[i][j] == "W") {
        // 이긴 경우
        winCount++
        gameCount++
        if (weights[i] < weights[j]) {
          winBiggerBoxer++
        }
      }
    }
    let percent = gameCount == 0 ? 0 : (winCount / gameCount) * 100
    boxersInfo[i] = [percent, winBiggerBoxer, i, weights[i]] // i는 복서의 번호 - 1
  }

  // console.log(boxersInfo)
  boxersInfo.sort(sortFunction)
  // console.log(boxersInfo)

  boxersInfo.map((boxer) => console.log(boxer[2] + 1))
}

solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]) // result [3,4,1,2]
solution([145, 92, 86], ["NLW", "WNL", "LWN"]) // result [2,3,1]
solution([60, 70, 60], ["NNN", "NNN", "NNN"]) // result [2,1,3]
