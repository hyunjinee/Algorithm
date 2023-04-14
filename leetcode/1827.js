function minOperations(nums) {
  let ans = 0
  for (let i = 0; i < nums.length - 1; i++) {
    const a = nums[i]
    const b = nums[i + 1]

    if (a < b) {
      continue
    }

    if (a === b) {
      nums[i + 1] += 1
      ans++
      continue
    }

    if (a > b) {
      while (nums[i] >= nums[i + 1]) {
        nums[i + 1] += 1
        ans++
      }
    }
  }

  return ans
}
