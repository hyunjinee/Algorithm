solution(80, [
  [80, 20],
  [50, 40],
  [30, 10],
]) // 3

function solution(k, dungeons) {
  const answer = []

  const visited = Array(dungeons.length).fill(false)

  function backTracking(count, k) {
    answer.push(count)

    for (let i = 0; i < dungeons.length; i++) {
      const [min, cost] = dungeons[i]

      if (min <= k && visited[i] == false) {
        visited[i] = true
        k = k - cost
        backTracking(count + 1, k)
        k = k + cost
        visited[i] = false
      }
    }
  }
  backTracking(0, k)

  return Math.max(...answer)
}
// function solution(k, dungeons) {
//   let answer = 0
//   const visited = Array(dungeons.length).fill(false)

//   backTracking(k, [])

//   function backTracking(k, can) {
//     if (k < 0) {
//       return
//     }

//     if (visited.reduce((a, x) => a + x) > answer) {
//       answer = can.length
//       return
//     }

//     for (let i = 0; i < dungeons.length; i++) {
//       const [min, cost] = dungeons[i]

//       if (min <= k && visited[i] == false) {
//         visited[i] = true
//         k = k - cost
//         can.push("temp")
//         backTracking(k, can)
//         can.pop()
//         k = k + cost
//         visited[i] = false
//       }
//     }
//   }

//   console.log(answer)
//   return answer
// }

// 현재 피로도 k와 던전별 최소 필요 필요도, 소모 필요도
// 현재 피로도 k
// 던전별 최소 필요 피로도, 소모 피로도
// 유저가 탐험할 수 있는 최대 던전 수를 return 해라.

// 하루에 한번 탐험. 최대한 많이 탐험하려면 어떻게 해야하는가?

// 1. 최소 필요 필요도는 적으면서 소모 피로도도 적은 던전을 탐험해
