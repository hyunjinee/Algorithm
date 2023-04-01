function solution(prices) {
  const upperCandidateIndex = []
  const lowerCandidateIndex = []

  for (let i = 1; i < prices.length - 1; i++) {
    if (prices[i] > prices[i - 1] && prices[i] > prices[i + 1]) {
      upperCandidateIndex.push([i, "상봉"])
    }

    if (prices[i] < prices[i - 1] && prices[i] < prices[i + 1]) {
      lowerCandidateIndex.push([i, "하봉"])
    }
  }
  console.log(upperCandidateIndex, lowerCandidateIndex)

  const candidate = [...upperCandidateIndex, ...lowerCandidateIndex]
  candidate.sort((a, b) => a[0] - b[0])
  // console.log(candidate)
  // 상봉과 하봉이 존재하는 위치를 찾았으므로, 각 봉의 너비를 구한후 배열에 넣는다.

  function calculateWidthOfSangBong(index) {
    let width1 = 0,
      width2 = 0,
      temp1 = prices[index],
      temp2 = prices[index]
    // 왼쪽 부터 탐색
    for (let i = index - 1; i >= 0; i--) {
      if (prices[i] < temp1) {
        temp1 = prices[i]
        width1++
      }
    }
    // 그 후 오른쪽 탐색
    for (let i = index + 1; i < prices.length; i++) {
      if (prices[i] < temp2) {
        temp2 = prices[i]
        width2++
      }
    }

    return Math.min(width1, width2)
  }

  function calculateWidthOfHaBong(index) {
    let width1 = 0,
      width2 = 0,
      temp1 = prices[index],
      temp2 = prices[index]
    // 왼쪽 부터 탐색
    for (let i = index - 1; i >= 0; i--) {
      if (prices[i] > temp1) {
        temp1 = prices[i]
        width1++
      }
    }
    for (let i = index + 1; i < prices.length; i++) {
      if (prices[i] > temp2) {
        temp2 = prices[i]
        width2++
      }
    }

    return -Math.min(width1, width2)
  }

  for (let [num, orientation] of candidate) {
    if (orientation == "상봉") {
      console.log(calculateWidthOfSangBong(num))
    } else if (orientation == "하봉") {
      console.log(calculateWidthOfHaBong(num))
    }
  }
}

// solution([12, 6, 6, 12, 6, 24, 30, 32, 34, 36, 24, 18, 6, 6, 18, 30, 6]) // [1,-1,3,1]
// solution([4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) // [-3, 3]
solution([1000, 2000, 3000, 2000, 3000, 4000, 3000]) // [1, -1, 1]

// 상봉과 하봉을 어떻게 찾아낼 것인가.
// 우선 상봉부터 생각해보자. 상봉은 왼쪽이 자신보다 작고 오른쪽도 자신보다 작아야한다.
// 극대가되는 지점이다.
// 우선 상봉과 하봉의 후보를 모두 찾는다.
