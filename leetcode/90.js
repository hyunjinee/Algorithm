/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsetsWithDup = function (nums) {
  nums.sort()
  const res = [[]]

  helper(nums, res, [], 0)
  return res
}

const helper = (nums, res, comb, start) => {
  for (let i = start; i < nums.length; i++) {
    if (i == start || nums[i] != nums[i - 1]) {
      comb.push(nums[i])
      res.push(comb.slice())
      helper(nums, res, comb, i + 1)
      comb.pop()
    }
  }
}
