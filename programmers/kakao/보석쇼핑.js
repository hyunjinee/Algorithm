function solution(gems) {
  const set = new Set(gems)
  const size = set.size
  let l = 0,
    r = 0
  let ans = [1, gems.length]
  const hit = new Map()

  hit.set(gems[0], 1)

  while (r < gems.length) {
    if (hit.size === size) {
      if (ans[1] - ans[0] > r - l) {
        ans = [l + 1, r + 1]
      }

      hit.set(gems[l], hit.get(gems[l]) - 1)

      if (hit.get(gems[l]) === 0) {
        hit.delete(gems[l])
      }

      l++
    } else {
      r++
      const right = hit.get(gems[r])
      hit.set(gems[r], right ? right + 1 : 1)
    }
  }
  return ans
}

// 이분탐색 풀이
// function solution(gems) {
//   let ans
//   const set = new Set()
//   for (const gem of gems) {
//     set.add(gem)
//   }
//   // 이 문제는 이분탐색

//   let left = 0
//   let right = gems.length - 1

//   while (left <= right) {
//     const mid = Math.floor((left + right) / 2)

//     const range = mid

//     let ok = false

//     for (let i = 0; i < gems.length; i++) {
//       const newSet = new Set(gems.slice(i, i + range + 1))
//       if (newSet.size === set.size) {
//         ok = true
//         if (ans && ans[1] - ans[0] > range) {
//           ans = [i, i + range]
//         } else if (ans && ans[1] - ans[0] === range) {
//           continue
//         } else if (!ans) {
//           ans = [i, i + range]
//         }
//         break
//       }
//     }

//     if (ok) {
//       right = mid - 1
//     } else {
//       left = mid + 1
//     }
//   }

//   console.log(ans)
// }

// 아래는 그냥 구현

// for (let i = 0; i < gems.length; i++) {
//   for (let j = i; j < gems.length; j++) {
//     const newSet = new Set(gems.slice(i, j + 1))
//     if (newSet.size === set.size) {
//       if (ans && ans[1] - ans[0] > j - i) {
//         ans = [i, j]
//       } else if (ans && ans[1] - ans[0] === j - i) {
//         continue
//       } else if (!ans) {
//         ans = [i, j]
//       }
//       break
//     }
//   }
// }
// return [ans[0] + 1, ans[1] + 1]
