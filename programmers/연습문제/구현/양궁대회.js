function solution(n, info) {
  let ans = -1
  let maxScore = -Infinity
  backTracking(Array(11).fill(0))

  function backTracking(arr) {
    if (arr.reduce((a, x) => a + x) === n) {
      console.log(arr)
      const [winner, score] = calculate(info, arr)
      if (winner === "lion") {
        if (maxScore < score) {
          ans = arr
        }
      }
      return
    }

    for (let i = 0; i < 11; i++) {
      arr[i] = arr[i] + 1
      backTracking(arr)
      arr[i] = arr[i] - 1
    }
  }

  if (ans === -1) {
    return [-1]
  }

  return ans
}

function calculate(peach, lion) {
  let peachScore = 0
  let lionScore = 0

  for (let i = 0; i < 11; i++) {
    if (peach[i] >= lion[i]) {
      peachScore += 10 - i
    } else {
      lionScore += 10 - i
    }
  }

  if (peachScore >= lionScore) {
    return ["peach", peachScore]
  } else {
    return ["lion", lionScore]
  }
}

// 라이언 vs 어피치

// 만약 k(k는 1~10사이의 자연수)점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우 더
// 많은 화살을 k 점에 맞힌 선수가 k점을 가져간다.

// 단 a == b일 경우 어피치가 k점을 가져간다.k점을 여러발 맞혀도 k 점보다 많은 점수를
// 가져가는게 아니고 k 점만 가져가는 것을 유의하자.

// 또한 a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k 점에 한발도 맞히지 못한 경우
// 어느 누구도 k 점을 가져가지 않는다.

// 최종 점수가 같으면 어피치가 우승

// 현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례다

// 라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n 발의 화살을 어떤 과녁 점수에
// 맞혀야 하는지를 구하려고 한다.

// 화살의 개수를 담은 자연수 n, 어피치가 맞힌 과녁의 점수를 담은 배열 info가 매개변수로
// 주어질 때 이때 라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁점수에
// 맞춰야 하는지를 10점부터 0점까지 순서대로 정수 배열에 담아 return 하도록 solution
// 함수를 작성하자

// 라이언이 우승할 수 없는 경우 (무조건 지거나 비기는 경우) -1을 담아 return 하자

solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) //  [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
