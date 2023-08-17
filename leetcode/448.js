/**
 * @param {number[]} nums
 * @return {number[]}
 */
const findDisappearedNumbers = function (nums) {
  const n = nums.length
  const ans = new Set(nums)
  const array = []
  for (let i = 1; i <= n; i++) {
    if (!ans.has(i)) {
      array.push(i)
    }
  }
  return array
}
