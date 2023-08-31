// Recursion, Memoization
const canPartition = function (nums) {
  let sum = nums.reduce((acc, cur) => acc + cur)
  if (sum % 2 === 1) {
    return false
  }
  sum /= 2
  let memo = new Map()
  return dfs(nums, sum, 0, memo)
  // T.C: O(M*N), M = half of sum, N = number of elements
  // S.C: O(M*N)
}

/*
Using only sum as key for hash table is sufficient instead of using both sum AND index
because of the following constraint, 1 <= nums[i] <= 100, and the fact that we are simply
storing boolean values. It is still safe to use the combination of index and sum as key.
*/

/*
Returns boolean value telling if nums[`idx`...end] has a subset sum of `sum`
*/
const dfs = (nums, sum, idx, memo) => {
  if (sum === 0) {
    return true
  }
  if (sum < 0 || idx === nums.length) {
    return false
  }
  if (memo.has(`${idx}-${sum}`)) {
    return memo.get(`${idx}-${sum}`)
  }
  // either include current element or skip
  let res = dfs(nums, sum - nums[idx], idx + 1, memo) || dfs(nums, sum, idx + 1, memo)
  memo.set(`${idx}-${sum}`, res)
  return res
}

// function canPartition(nums) {
//   const total = nums.reduce((a, x) => a + x, 0)

//   if (total % 2 !== 0) return false

//   const target = total / 2

//   const dp = Array(target + 1).fill(false)

//   dp[0] = true

//   for (const num of nums) {
//     for (let i = target; i >= 0; i--) {
//       if (dp[i]) {
//         dp[i + num] = true
//       }
//     }
//   }

//   if (dp[target]) return true
//   return false
// }
// console.log(canPartition([1, 5, 11, 5]))

// // var canPartition = function(nums) {
// //   if(!nums) return false
// //   let total = nums.reduce((a,b) => a + b, 0)

// //   if(total%2 != 0) return false

// //   let target = total /2
// //   let arr = new Array(target + 1).fill(false)
// //   arr[0] = true

// //   for(let el of nums) {

// //       for(let i = target; i >=0; i--) {
// //           let complement = i - el

// //           if(!arr[i] && arr[complement]){
// //               arr[i] = true
// //           }
// //           if(arr[target] == true) return true
// //       }
// //   }

// //   return false
// // };

// // backtracking 시간초과
// // /**
// //  * @param {number[]} nums
// //  * @return {boolean}
// //  */
// // const canPartition = function (nums) {
// //   const sum = nums.reduce((a, x) => a + x, 0)
// //   const visited = Array(nums.length).fill(false)
// //   let flag = false

// //   backTracking([])

// //   function backTracking(curr) {
// //     const sum1 = curr.reduce((a, x) => a + x, 0)
// //     if (sum1 === sum - sum1) {
// //       flag = true
// //       return
// //     }

// //     for (let i = 0; i < nums.length; i++) {
// //       if (visited[i]) continue

// //       visited[i] = true
// //       backTracking([...curr, nums[i]])
// //       visited[i] = false
// //     }
// //   }

// //   return flag
// // }
