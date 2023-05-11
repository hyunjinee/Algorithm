const maxUncrossedLines = function (A, B) {
  const m = A.length
  const n = B.length

  const dp = new Array(m + 1)

  for (let i = 0; i <= m; i++) {
    dp[i] = new Array(n + 1).fill(0)
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (A[i - 1] === B[j - 1]) {
        dp[i][j] = 1 + dp[i - 1][j - 1]
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
      }
    }
  }

  return dp[m][n]
}

// const maxUncrossedLines = (nums1, nums2) => {
//   // 현재 인덱스에서 연결 할 것인가 하지 않을 것인가
//   // 두가지 선택이 존재한다

//   const dp = Array.from({ length: nums1.length }, () => 0)

//   for (let i = 0; i < nums1.length; i++) {
//     if (nums2.length < i) {
//       continue
//     }
//     const up = nums1[i]
//     const down = nums2[i]

//     if (up === down) {
//       dp[i] = dp[i - 1] + 1
//     }
//   }

//   console.log(dp)
// }

// console.log(maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
