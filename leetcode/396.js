const maxRotateFunction = function (nums) {
  const sum = nums.reduce((acc, cur) => acc + cur)
  let fx = nums.reduce((acc, cur, idx) => acc + cur * idx, 0),
    maxF = fx

  for (let i = nums.length - 1; i > 0; i--) {
    fx += sum - nums.length * nums[i]
    maxF = Math.max(maxF, fx)
  }

  return maxF
}

// 시간 복잡도 O(n^2)
// /**
//  * @param {number[]} nums
//  * @return {number}
//  */
// const maxRotateFunction = function (nums) {
//   if (nums.length === 1) {
//     return 0
//   }

//   const count = nums.length - 1
//   let ans = nums.reduce((a, x, i) => a + x * i, 0)

//   for (let i = 0; i < count; i++) {
//     nums.unshift(nums.pop())
//     const result = nums.reduce((a, x, i) => a + x * i, 0)

//     console.log(nums, result)
//     ans = Math.max(ans, result)
//   }

//   return ans
// }
